# Exporting file provider metrics data

**Framework**: File Provider

Download and analyze usage, consistency, and error data.

#### Overview

Use CloudKit Console to create a data export token that you use to export file provider metrics for your apps. Request data from iCloud web services, and download the data when the request is complete. For more information on CloudKit and CloudKit Console, see [`Build apps using CloudKit`](https://developer.apple.comhttps://developer.apple.com/icloud/cloudkit/).

You can download three different reports that provide file provider metrics:

- **Consistency**: A summary of the state of the file provider domain, gathered daily by the system’s consistency checker. This report also contains information on one item from the pending set that’s encountered an error. The *pending set* contains any items in the file provider that haven’t synced for over a minute. The *super pending set* contains any items in either the file provider or the filesystem that haven’t synced for over a minute.
- **Usage**: A summary of the kinds of items that a file provider stores on someone’s device, along with the number of materialized items, dataless items, and the total space used by items. A *materialized item* is an item for which the system stores content on someone’s device. A *dataless item* is an item that the system synchronizes on the device, and downloads the content on demand when someone opens it.
- **Dynamic errors**: A list of errors that occurred during file provider operations, along with additional details you can use to investigate the errors.

> **Note**:  If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > CloudKit Console > Data Export [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

##### Create a Data Export Token

To access log data for your apps, create a data export token by following these steps:

1. Navigate to [`CloudKit Console settings`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/notifications/teams?settings=account) and log in.
2. Click Tokens.
3. Click Create Data Export Token.
4. Give the token a name, and an optional description.
5. Choose the bundle identifier for the app for which you want to download data.
6. Choose the data set you want to download.
7. Set an expiration date for the token, up to a maximum of 6 months in the future.
8. Click Create Data Export Token.
9. Securely store the token you create in step 8.

> **Note**:  If you navigate back to the CloudKit Console later, you can’t see the data export token’s value again.

The token you create is restricted to your developer account, and only gives you access to the data set you requested for the specified app.

##### Create a Data Export Request

Make an HTTPS `POST` request to the data export request endpoint:

- `https://api.icloud.apple.com/v1/dataExports/fpfs/teams/{teamId}/appId/{appId}/datasetName/{dataset}/request`

Substitute these values:

- **`{teamId}`**: Your Apple Developer team identifier.
- **`{appId}`**: Your app’s bundle identifier.
- **`{dataset}`**: To request a consistency report, use `consistency`. To request a usage report, use `usage`. To request a dynamic errors report, use `dynamicerrors`.

Supply your data export token in the `X-Apple-CloudKit-Management-Token` header, and provide a JSON object in the body with these fields:

- **`startDate`**: The earliest date for which to include data, in the format `yyyy-MM-dd`. The date needs to be 90 or fewer days in the past.
- **`endDate`**: The latest date for which to include data, in the format `yyyy-MM-dd`. The date needs to be 1–30 days after `startDate`, and one or more days in the past.
- **`dataDownloadUrlExpiresInMinutes`**: The number of minutes after you receive the download for which the download URL needs to remain valid, between `20` and `60`.

The server responds with a JSON object that contains these fields:

- **`statusUrl`**: A URL you use to check the status of your request.
- **`requestedAt`**: The time at which you requested the data export, in ISO8601 format.

```shell
% curl -X POST \
-H "Content-Type: application/json" \
-H "X-Apple-CloudKit-Management-Token: {data-export-token}" \
-d \
'{
"startDate": "2024-01-01",
"endDate": "2024-01-26",
"dataDownloadUrlExpiresInMinutes": 60
}' https://api.icloud.apple.com/v1/dataExports/fpfs/teams/{teamId}/appId/{appId}/datasetName/{dataset}/request 

{
"statusUrl": "https://example.com/statusURL",
"requestedAt": "2024-02-14T18:32:30.947451Z"
}
```

The data export request endpoint might return the following HTTP status codes that represent errors:

- **`400`**: The request is badly formed.
- **`401`**: The data export token is invalid.
- **`500`**: An internal error occurred.

You can request a download that covers the same date range as a previous download. If you make a repeat request within 24 hours, the server returns the same status URL as the original request.  If you make a repeat request after 24 hours, the server creates a new request with a new status URL, and any events within the requested time range that are logged after the original request was made are included in the new report.

> **Note**:  The status URLs for all requests are available for 6 months after you make the request. Make sure you use the latest URLs for checking status and downloading reports.

##### Check the Status of Your Data Export

Make an HTTPS `GET` request to the status URL, passing your data export token in the `X-Apple-CloudKit-Management-Token` header.

The server responds with a JSON object that contains these fields:

- **`status`**: One of these four strings: `PROCESSING`, `FAILED`, `EXPIRED`, or `SUCCESS`.
- **`requestedAt`**: The time at which you requested the data export, in ISO8601 format.
- **`downloadDetails`**: If the status is `PROCESSING`, `EXPIRED`, or `FAILED`, this key isn’t set. If the status is `SUCCESS`, it’s a JSON object that contains `dataUrl`, the URL you use to get the exported data; and `expiresAt`, the time at which the data URL expires.

Apple servers retain the exported data for 6 months. To re-download the data, make another `GET` request to the status URL and download the data from the new download URL.

```shell
% curl -X GET -H "X-Apple-CloudKit-Management-Token: {data-export-token}" https://example.com/statusURL
{
    "requestedAt": "2024-02-14T18:32:30.947Z",
    "status": "SUCCESS",
    "downloadDetails": {
        "dataUrl": "https://example.com/download/data.csv",
        "expiresAt": "2024-02-14T18:53:14.762922Z"
    }
}
```

The data export status endpoint might return the following HTTP status codes that represent errors:

- **`400`**: The request is badly formed.
- **`404`**: The data export token is invalid.
- **`500`**: An internal error occurred.

##### Download the Exported Data

Make an HTTPS `GET` request to URL in the status object’s `downloadDetails.dataUrl` field to receive a CSV file that contains your exported data:

```shell
curl --compressed -X GET "https://example.com/download/data.csv" -o export.csv
```

##### Analyze the Csv File

The CSV file for all types of report contains these common fields:

- **`_build`**: A string that represents the operating system build number, for example, `21D61`.
- **`_internal`**: An integer that’s `0` when `_build` is a released build, or `2` when it’s a public seed build.
- **`_osversion`**: A string that’s the operating system release version, for example, `17.3.1`.
- **`_osname`**: A string that’s the name of the operating system, for example, `iOS`.
- **`_productfamily`**: A string that’s the name of the product family, for example, `iPhone`.
- **`provider`**: A string that’s the bundle identifier of the file provider.
- **`eventtime`**: A date that’s the timestamp of the event, in the format `yyyy-MM-dd`.
- **`providerversion`**: A string that’s the version of the file provider extension.

##### Understand Usage Report Fields

The usage report contains these fields:

- **`materialized_reg`**: An integer that’s the number of materialized regular files.
- **`materialized_pkg`**: An integer that’s the number of materialized packages.
- **`materialized_dir`**: An integer that’s the number of materialized directories.
- **`materialized_als`**: An integer that’s the number of materialized aliases.
- **`materialized_sym`**: An integer that’s the number of materialized symlinks.
- **`dataless_reg`**: An integer that’s the number of dataless regular files.
- **`dataless_pkg`**: An integer that’s the number of dataless packages.
- **`dataless_dir`**: An integer that’s the number of dataless directories.
- **`total_vol_reg`**: An integer that’s the total size of regular items, in bytes.
- **`total_vol_pkg`**: An integer that’s the total size of packages, in bytes.
- **`disconnection_state`**: An enum that indicates whether the file provider domain is connected, and if it’s disconnected, the reason. For a list of values this field can take, see the section, “Understand the disconnection states”, below.
- **`wharf_global_size`**: An integer that’s the size in bytes of the location that file provider uses to stage uploads and downloads for the domain.
- **`wharf_global_count`**: An integer that’s the number of files in the location that file provider uses to stage uploads and downloads for the domain.
- **`enabled`**: A boolean that’s `true` if someone enabled the file provider domain; otherwise, it’s `false`.
- **`pinned_resident_pct`**: A string that’s the fraction of storage used by materialized documents that are also pinned, expressed as a percentage, and takes one of these values: `0%`, `< 1%`, `<30 %`, `< 100%`, or `100%`.
- **`sync_pause_item_count`**: An Boolean that’s `true` if more than one item’s synchronization is paused due to an active iWork collaboration session; otherwise, it’s `false`.

##### Understand Dynamic Error Fields

The dynamic errors report contains these fields:

- **`operationtype`**: A string that identifies the type of operation.
- **`operationside`**: A string that’s `FS` if the operation is a disk operation, or `FP` if it’s an extension operation.
- **`operationduration`**: An integer that’s the operation duration in milliseconds.
- **`errordomain`**: A string that’s the error domain.
- **`errorcode`**: An integer that’s the error code.
- **`underlyingerrordomain`**: A string that’s the error domain of an underlying error.
- **`underlyingerrorcode`**: An integer that’s the error code of an underlying error.
- **`moreunderlyingerrors`**: An integer that’s `1` if there are more underlying errors; otherwise, it’s `null`.
- **`itemtype`**: A string that identifies the type of the item.
- **`commonfolder`**: A string that identifies the folder as a common folder, for example `Root` or `Trash`. If the folder isn’t a common folder, it’s `null`.
- **`itemsize`**: An integer that’s the size of the item, in bytes.
- **`childitemcount`**: An integer that’s the number of items in the directory.
- **`connectiontype`**: A string that identifies the connection type as `wifi` or `cellular`.
- **`reimportwithreason`**: A string that represents the reason for the current reimport, or `null` if the operation isn’t a reimport.
- **`reason`**: An integer that’s a 37-bit bitfield that identifies the reason for the operation. For a list of values this field can take, see the section, “Understand the transfer operation types and operation reasons”, below.

##### Understand Consistency Report Fields

The consistency report contains these fields:

- **`accumulatederrors`**: An integer that’s the total number of errors detected by the consistency checker.
- **`accumulateddomains`**: An integer that’s the number of domains set up on disk.
- **`accumulatedfilesizes`**: An integer that’s the total size of files, in bytes.
- **`accumulatedsizeofdisk`**: An integer that’s the total disk space used, in bytes.
- **`accumulatedsuccesses`**: An integer that’s the total number of consistent files.
- **`numberofbrokenfilesinfssnapshotandfpsnapshotcheck`**: An integer that’s the total number of inconsistent files in the file provider database.
- **`numberoffileschecked`**: An integer that’s the total number of items the consistency checker checked.
- **`numberofitemsinfpsnapshot`**: An integer that’s the total number of items recorded in the file provider database from the provider.
- **`numberofitemsinfssnapshot`**: An integer that’s the total number of items recorded in the file provider database that are on disk.
- **`numberofitemsondisk`**: An integer that’s the total number of items stored on disk.
- **`operationside`**: A string that’s `FP` if an operation failed in the file provider extension; or `FS` if the operation failed on disk.
- **`pendingseterrors`**: A dictionary where the keys are errors that happened to items in the pending set, and the values are counts of those errors. The dictionary contains at most 5 keys.
- **`pendingsetsize`**: An integer that’s the total number of items that haven’t synced for at least 1 minute.
- **`fpckrunreason`**: A string that identifies why the consistency checker ran.
- **`totaldatalessitems`**: An integer that’s the total number of dataless items.
- **`totalmaterializeditems`**: An integer that’s the total number of materialized items.
- **`totalfixeddiskbrokeninvariants`**: An integer that’s the total number of items on disk that the consistency checker fixed.
- **`totalfixedfssnapshotdiffs`**: An integer that’s the total number of items in the file provider database that the consistency checker fixed.
- **`samplingrate`**: A floating-point number that indicates the fraction of items sampled by the consistency checker. If it’s `1.0`, then the consistency checker sampled all items.
- **`isinreimport`**: An integer that indicates whether the system is currently reimporting the file provider domain.
- **`multiplehardlinksextensions`**: A comma-separated list of obfuscated file extensions for items in the domain that have hard links.
- **`brokeninvarianthaswrongprotectionclass`**: An integer that’s the number of items where the consistency checker detected the wrong protection class.
- **`brokeninvariantisbrmfullymaterialized`**: An integer that’s the number of fully materialized items that have a byte range materialization marker.
- **`disk_broken_invariants_could_not_open`**: An integer that’s the number of items on disk that the system was unable to open.
- **`disk_broken_invariants_dataless_file_in_ignored_folder`**: An integer that’s the number of dataless files in ignored folders on disk.
- **`disk_broken_invariants_evictable_file_in_ignored_folder`**: An integer that’s the number of evictable files in ignored folders on disk.
- **`disk_broken_invariants_detached_root_with_stale_bookmark`**: An integer that’s the number of detached roots with a stale bookmark on disk.
- **`disk_broken_invariants_detached_root_without_sync_root_bit`**: An integer that’s the number of detached roots without a sync root bit on disk.
- **`disk_broken_invariants_detached_root_without_valid_bookmark`**: An integer that’s the number of detached roots without a valid bookmark on disk.
- **`disk_broken_invariants_embedded_detached_root`**: An integer that’s the number of embedded detached roots on disk.
- **`disk_broken_invariants_embedded_detached_root_in_package`**: An integer that’s the number of embedded detached roots in packages on disk.
- **`disk_broken_invariants_file_has_more_than_one_hardlink`**: An integer that’s the number of files on disk with more than one hardlink.
- **`disk_broken_invariants_files_with_external_hardlinks`**: An integer that’s the number of files on disk with external hardlinks.
- **`disk_broken_invariants_files_with_multiple_hardlinks`**: This field is always `null`.
- **`disk_broken_invariants_files_with_multiple_hardlinks_extensions`**: An integer that’s the number of files on disk with multiple hardlinks extensions.
- **`disk_broken_invariants_has_decmpfs_xattr_but_not_evictable`**: An integer that’s the number of files on disk that have the `com.apple.decmpfs` extended attribute and aren’t evictable.
- **`disk_broken_invariants_has_flag_without_decmpfs_xattr`**: An integer that’s the number of dataless files on disk without the `com.apple.decmpfs` extended attribute.
- **`disk_broken_invariants_has_invalid_decmpfs_xattr`**: An integer that’s the number of files on disk with invalid `com.apple.decmpfs` extended attributes.
- **`disk_broken_invariants_has_invalid_favorite_rank`**: An integer that’s the number of files on disk with invalid favorite ranks.
- **`disk_broken_invariants_has_invalid_last_used_date`**: An integer that’s the number of files on disk with invalid last-used dates.
- **`disk_broken_invariants_has_invalid_tag_data`**: An integer that’s the number of files on disk with invalid tag data.
- **`disk_broken_invariants_has_uf_compressed_flag_without_sf_dataless`**: An integer that’s the number of files on disk that have the `UF_COMPRESSED` flag and don’t have the `SF_DATALESS` flag.
- **`disk_broken_invariants_has_wrong_protection_class`**: An integer that’s the number of files on disk that have the wrong protection class.
- **`disk_broken_invariants_ignored_file_is_evictable`**: An integer that’s the number of evictable, ignored files on disk.
- **`disk_broken_invariants_ignored_folder_in_ignored_folder_has_sync_root_bit_set`**: An integer that’s the number of ignored folders on disk that are in ignored folders and have the sync root bit set.
- **`disk_broken_invariants_ignored_folder_missing_sync_root_bit`**: An integer that’s the number of ignored folders on disk that are missing the sync root bit.
- **`disk_broken_invariants_is_dataless_directory_with_data`**: An integer that’s the number of dataless directories on disk that contain data.
- **`disk_broken_invariants_is_dataless_file_with_data`**: An integer that’s the number of dataless files on disk that contain data.
- **`disk_broken_invariants_is_dataless_package_item`**: An integer that’s the number of dataless packages on disk.
- **`disk_broken_invariants_is_directory_duplicate`**: An integer that’s the number of directory duplicates on disk.
- **`disk_broken_invariants_is_empty_dir_with_extension`**: An integer that’s the number of empty directories on disk that have an extension.
- **`disk_broken_invariants_is_empty_file`**: An integer that’s the number of empty files on disk.
- **`disk_broken_invariants_is_empty_package`**: An integer that’s the number of empty packages on disk.
- **`disk_broken_invariants_is_evictable_package_item`**: An integer that’s the number of evictable package items on disk.
- **`disk_broken_invariants_is_evictable_without_decmpfs_xattr`**: An integer that’s the number of evictable files on disk that don’t have a `com.apple.decmpfs` extended attribute.
- **`disk_broken_invariants_is_evictable_without_flags`**: An integer that’s the number of evictable files on disk that don’t have flags.
- **`disk_broken_invariants_is_file_duplicate`**: An integer that’s the number of duplicate files on disk.
- **`disk_broken_invariants_is_filled_with_zeros`**: An integer that’s the number of files on disk that are filled with zeros.
- **`disk_broken_invariants_is_neither_dataless_nor_evictable_nor_pinned`**: An integer that’s the number of files on disk that are not not dataless, not evictable, and not pinned.
- **`disk_broken_invariants_is_owned_by_other`**: An integer that’s the number of files on disk that are owned by the `other` account.
- **`disk_broken_invariants_is_owned_by_root`**: An integer that’s the number of files on disk that are owned by the `root` account.
- **`disk_broken_invariants_is_package_duplicate`**: An integer that’s the number of duplicate packages on disk.
- **`disk_broken_invariants_is_purgeable_not_evictable`**: An integer that’s the number of files on disk that are purgeable and not evictable.
- **`disk_broken_invariants_is_side_fault`**: An integer that’s the number of side-fault files on disk.
- **`disk_broken_invariants_is_tracked_but_docid_is_stale`**: An integer that’s the number of files on disk that are tracked and have a stale `docID`.
- **`disk_broken_invariants_is_tracked_but_docid_is_unknown`**: An integer that’s the number of files on disk that are tracked and have an unknown `docID`.
- **`disk_broken_invariants_is_tracked_but_docid_is_zero`**: An integer that’s the number of files on disk that are tracked and have `0` as the value for their `docID`.
- **`disk_broken_invariants_is_tracked_but_fileid_mismatch`**: An integer that’s the number of files on disk that are tracked and have a mis-matched `fileID`.
- **`disk_broken_invariants_is_tracked_but_should_not_be`**: An integer that’s the number of files on disk that are tracked and don’t need to be on the disk.
- **`disk_broken_invariants_is_untracked_but_should_be`**: An integer that’s the number of files that aren’t tracked and need to be on the disk.
- **`disk_broken_invariants_package_has_sync_root_bit`**: An integer that’s the number of packages on disk that have the sync root bit.
- **`remaining_disk_broken_invariants_could_not_open`**: An integer that’s the number of items on disk that the system couldn’t open after running the repair tool.
- **`remaining_disk_broken_invariants_dataless_file_in_ignored_folder`**: An integer that’s the number of dataless files on disk that are in ignored folders after running the repair tool.
- **`remaining_disk_broken_invariants_detached_root_with_stale_bookmark`**: An integer that’s the number of detached roots with stale bookmarks on disk after running the repair tool.
- **`remaining_disk_broken_invariants_detached_root_without_sync_root_bit`**: An integer that’s the number of detached roots on disk without the sync root bit set after running the repair tool.
- **`remaining_disk_broken_invariants_detached_root_without_valid_bookmark`**: An integer that’s the number of detached roots on disk that don’t have valid bookmarks after running the repair tool.
- **`remaining_disk_broken_invariants_embedded_detached_root`**: An integer that’s the number of embedded detached roots on disk after running the repair tool.
- **`remaining_disk_broken_invariants_embedded_detached_root_in_package`**: An integer that’s the number of embedded detached roots in packages on disk after running the repair tool.
- **`remaining_disk_broken_invariants_evictable_file_in_ignored_folder`**: An integer that’s the number of evictable files in ignored folders on disk after running the repair tool.
- **`remaining_disk_broken_invariants_has_decmpfs_xattr_but_not_evictable`**: An integer that’s the number of files on disk that have a `com.apple.decmpfs` extended attribute and aren’t evictable, after running the repair tool.
- **`remaining_disk_broken_invariants_has_flag_without_decmpfs_xattr`**: An integer that’s the number of files on disk that have the dataless flag and don’t have a `com.apple.decmpfs` extended attribute, after running the repair tool.
- **`remaining_disk_broken_invariants_has_invalid_decmpfs_xattr`**: An integer that’s the number of files on disk that have invalid `com.apple.decmpfs` extended attributes after running the repair tool.
- **`remaining_disk_broken_invariants_has_invalid_favorite_rank`**: An integer that’s the number of files on disk that have invalid favorite ranks after running the repair tool.
- **`remaining_disk_broken_invariants_has_invalid_last_used_date`**: An integer that’s the number of files on disk that have invalid last-used dates after running the repair tool.
- **`remaining_disk_broken_invariants_has_invalid_tag_data`**: An integer that’s the number of files on disk that have invalid tag data after running the repair tool.
- **`remaining_disk_broken_invariants_has_uf_compressed_flag_without_sf_dataless`**: An integer that’s the number of files on disk that have the `UF_COMPRESSED` flag and don’t have the `SF_DATALESS` flag, after running the repair tool.
- **`remaining_disk_broken_invariants_has_wrong_protection_class`**: An integer that’s the number of files on disk that have the wrong protection class after running the repair tool.
- **`remaining_disk_broken_invariants_ignored_file_is_evictable`**: An integer that’s the number of ignored files on disk that are evictable, after running the repair tool.
- **`remaining_disk_broken_invariants_ignored_folder_missing_sync_root_bit`**: An integer that’s the number of ignored folders on disk that are missing the sync root bit, after running the repair tool.
- **`remaining_disk_broken_invariants_is_dataless_directory_with_data`**: An integer that’s the number of dataless directories on disk that contain data, after running the repair tool.
- **`remaining_disk_broken_invariants_is_dataless_file_with_data`**: An integer that’s the number of dataless files on disk that contain data, after running the repair tool.
- **`remaining_disk_broken_invariants_is_dataless_package_item`**: An integer that’s the number of dataless packages on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_directory_duplicate`**: An integer that’s the number of duplicate directories on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_empty_dir_with_extension`**: An integer that’s the number of empty directories on disk that have extensions, after running the repair tool.
- **`remaining_disk_broken_invariants_is_empty_file`**: An integer that’s the number of empty files on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_empty_package`**: An integer that’s the number of empty packages on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_evictable_package_item`**: An integer that’s the number of evictable packages on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_evictable_without_decmpfs_xattr`**: An integer that’s the number of evictable files on disk that don’t have a `com.apple.decmpfs` extended attribute, after running the repair tool.
- **`remaining_disk_broken_invariants_is_evictable_without_flags`**: An integer that’s the number of evictable files on disk that don’t have flags, after running the repair tool.
- **`remaining_disk_broken_invariants_is_file_duplicate`**: An integer that’s the number of duplicate files on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_filled_with_zeros`**: An integer that’s the number of files on disk that are filled with zeros, after running the repair tool.
- **`remaining_disk_broken_invariants_is_neither_dataless_nor_evictable_nor_pinned`**: An integer that’s the number of files on disk that are not dataless, not evictable, and not pinned, after running the repair tool.
- **`remaining_disk_broken_invariants_is_owned_by_other`**: An integer that’s the number of files on disk that are owned by the `other` account after running the repair tool.
- **`remaining_disk_broken_invariants_is_owned_by_root`**: An integer that’s the number of files on disk that are owned by the `root` account after running the repair tool.
- **`remaining_disk_broken_invariants_is_package_duplicate`**: An integer that’s the number of duplicate packages on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_purgeable_not_evictable`**: An integer that’s the number of files on disk that are purgeable and not evictable, after running the repair tool.
- **`remaining_disk_broken_invariants_is_side_fault`**: An integer that’s the number of side-fault files on disk after running the repair tool.
- **`remaining_disk_broken_invariants_is_tracked_but_docid_is_stale`**: An integer that’s the number of files on disk that are tracked and have a stale `docID`, after running the repair tool.
- **`remaining_disk_broken_invariants_is_tracked_but_docid_is_unknown`**: An integer that’s the number of files on disk that are tracked and have an unknown `docID`, after running the repair tool.
- **`remaining_disk_broken_invariants_is_tracked_but_docid_is_zero`**: An integer that’s the number of files on disk that are tracked and have `0` as their `docID`, after running the repair tool.
- **`remaining_disk_broken_invariants_is_tracked_but_fileid_mismatch`**: An integer that’s the number of files that are tracked and have a mismatched `fileID`, after running the repair tool.
- **`remaining_disk_broken_invariants_is_tracked_but_should_not_be`**: An integer that’s the number of files on disk that are tracked and don’t need to be on disk, after running the repair tool.
- **`remaining_disk_broken_invariants_is_untracked_but_should_be`**: An integer that’s the number of files that need to be tracked and aren’t on disk, after running the repair tool.
- **`database_creation_reason`**: A string that describes the reason that the file provider domain database was created.
- **`vendor_item_count_per_effective_policy`**: A JSON object that contains the following keys that all have Boolean values: - **`vendor_effective_keep_downloaded_policy_items`**: Value is `true` if the file provider has an effective policy to eagerly download and keep any item; otherwise, it’s `false`.
- **`vendor_effective_lazy_policy_items`**: Value is `true` if the file provider has an effective policy to lazily download any item; otherwise, it’s `false`.
- **`vendor_effective_evict_on_remote_update_policy_items`**: Value is `true` if the file provider has an effective policy to lazily download any item and evict it when it gets updated remotely; otherwise, it’s `false`.
- **`vendor_item_count_per_policy`**: A JSON object that contains the following keys that all have Boolean values: - **`vendor_keep_downloaded_policy_items`**: Value is `true` if the file provider has a policy to eagerly download and keep any item; otherwise, it’s `false`.
- **`vendor_lazy_policy_items`**: Value is `true` if the file provider has a policy to lazily download any item; otherwise, it’s `false`.
- **`vendor_evict_on_remote_update_policy_items`**: Value is `true` if the file provider has a policy to lazily download any item and evict it when it gets updated remotely; otherwise, it’s `false`.
- **`vendor_missing_allows_evict_capability_items`**: A Boolean that’s `true` if any item doesn’t have the flag that indicates that evicting the item is allowed; otherwise, it’s `false`.
- **`numberOfReconciliationTableEntries`**: An integer that’s the number of items represented in the file provider’s reconciliation table, including items in the working set and items on disk.
- **`reportAge`**: An integer that’s the number of days since the last time the file provider check ran successfully.

Additionally, the consistency report includes a randomly chosen instance of an error that the consistency checker encountered. It contains the following fields:

- **`apfs_available_space`**: An integer that’s the available disk space, in bytes.
- **`apfs_block_size`**: An integer that’s the block size used by the domain on the APFS volume, in bytes.
- **`apfs_encrypted`**: An integer that’s `1` if the volume is encrypted; otherwise, it’s `null`.
- **`diag_error_domain`**: A string that’s the domain of the randomly chosen error.
- **`diag_error_code`**: An integer that’s the code of the randomly chosen error.
- **`diag_underlying_error_domain`**: A string that’s the domain of the error that underlies the randomly chosen error.
- **`diag_underlying_error_code`**: An integer that’s the code of the error that underlies the randomly chosen error.
- **`apfs_flags`**: A bitfield that indicates the flags returned by `fstatfs(_:_:)` for the item.
- **`days_since_sync_engine_was_stable`**: An integer that’s the number of days since synchronization completed without an error.
- **`db_error_code`**: An integer that’s the code for an error that happened while gathering information.
- **`db_error_date`**: An integer that’s the logarithm in base 12 of the number of seconds that the item has been in the super pending set, rounded to the nearest whole number.
- **`db_error_domain`**: A string that’s the domain for an error that happened while gathering information.
- **`db_capabilities`**: An integer that enumerates the item’s [`NSFileProviderItemCapabilities`](nsfileprovideritemcapabilities.md).
- **`db_effective_content_policy`**: An integer that’s the content policy of the item.
- **`db_error_retry_count`**: An integer that counts the number of operation retries since the item entered an error state.
- **`db_fp_content_status`**: An integer that’s the server’s content-monitoring status for the item.
- **`db_fp_deletion_status`**: An integer that’s the server’s deletion status for the item.
- **`db_fs_content_status`**: An integer that’s the disk’s content-monitoring status for the item.
- **`db_fs_deletion_status`**: An integer that’s the disk’s deletion status for the item.
- **`db_fs_import_status`**: An integer that’s the import — or re-import — status for the item.
- **`db_is_package`**: An integer that indicates whether the item is a package.
- **`db_is_super`**: An integer that indicates whether the item is part of the super pending set.
- **`db_sharing_state`**: An integer that’s the sharing state of the item.
- **`db_transfer_error_domain`**: A string that’s the domain of the item’s latest transfer error.
- **`db_transfer_error_code`**: An integer that’s the code of the item’s latest transfer error.
- **`db_transfer_error_is_download`**: An integer that indicates whether the latest transfer error happened during a download.
- **`db_transfer_operation_type`**: An integer that enumerates the operation type. The possible values are listed in the section, “Understand the transfer operation types and operation reasons”, below.
- **`db_transfer_state`**: A bitfield that indicates the item’s transfer state. Bit 0 indicates whether the item was uploading; bit 1 indicates whether it was uploaded; bit 2 indicates whether it was downloading; and bit 3 indicates whether it was downloaded.
- **`eventtime`**: A date that’s the timestamp of the event, in the format `yyyy-MM-dd`.
- **`name_characters_sets`**: A bitfield that indicates whether the item’s name contains characters from particular sets. The bit masks are listed in the section, “Understand the character set bit masks”, below.
- **`name_extension`**: A string that’s a partially obfuscated version of the file extension, for example, `p{1}d`.
- **`name_is_apple_double`**: An integer that indicates whether the item’s name starts with `._` which marks the file as an Apple double file.
- **`name_is_dot_file`**: A boolean that’s `true` if the item’s name starts with a dot (`.`), and false otherwise.
- **`name_length`**: An integer that’s the length of the item’s name.
- **`name_path_depth`**: An integer that’s the item’s path depth.
- **`name_path_length`**: An integer that’s the length of the item’s path.
- **`name_unicode_norm`**: A string that indicates how the Unicode name of the item is normalized: if the name has the decomposed canonical form, it’s `D`; it the name has the precomposed canonical form, it’s `C`; if the name has a decomposed compatible form; it’s `KD`; if the name has a precomposed compatible form, it’s `KC`; otherwise, it’s undefined.
- **`name_uttype`**: A string that’s the item’s [`UTTypeReference`](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference).
- **`purge_atime`**: An integer that’s the purgeability access time of the item.
- **`purge_flags`**: An integer that’s the flags the system uses to mark the item purgeable.
- **`purge_gencount`**: An integer that’s the item’s generation count for being marked purgeable.
- **`purge_syncroot`**: An integer that’s the inode number of the root of the synchronization hierarchy for which the filesystem marked the item purgeable.
- **`reimportwithreason`**: A string that’s the reason for reimporting the item, or empty if the item isn’t reimported.
- **`stat_bsd_flags`**: A bitfield that’s the flags returned by `stat()` for the item’s file system.
- **`stat_btime`**: An integer that’s the item’s birth timestamp, reported by `stat()`.
- **`stat_btime_is_busy`**: An integer that indicates whether the item’s birth timestamp is equal to the value used by Finder to indicate it’s busy.
- **`stat_closest_syncroot`**: An integer that identifies the root of the item’s synchronization hierarchy. If the synchronization root is the domain’s main synchronization root, then it’s `0`; if the item has another synchronization root, it’s `2`; if the system didn’t find the synchronization root for the item, this value isn’t defined.
- **`stat_data_protection_class`**: An integer that’s the item’s data-protection class.
- **`stat_dir_entrycount`**: An integer that’s the number of items in the directory, reported by `stat()`.
- **`stat_finder_info_flags`**: A bitmask that indicates the Finder flags for the item. Bit 1 is set if the item is an alias; bit 2 is set if the item is a bundle; bit 3 is set if the item is invisible; bit 4 is set if the item has a hidden extension; and bit 5 is set if the item has a custom icon.
- **`stat_gencount`**: An integer that’s the item’s generation count, reported by `stat()`.
- **`stat_has_more_links`**: An integer that indicates whether the item has more links on disk, reported by `stat()`.
- **`stat_is_dirstat_enabled`**: An integer that’s the item’s recursive `dirstat` enablement state on an APFS filesystem, reported by `stat()`.
- **`stat_is_trash`**: An integer that indicates whether the item is in the trash, reported by `stat()`.
- **`stat_item_acl_count`**: An integer that’s the number of access control list rules on the item, reported by `stat()`.
- **`stat_logical_size`**: An integer that’s the logical size of the item on disk, reported by `stat()`.
- **`stat_mode`**: An integer that’s the item’s mode, reported by `stat()`.
- **`stat_mtime`**: An integer that’s the item’s modification timestamp, reported by `stat()`.
- **`stat_parent_acl_count`**: An integer that’s the number of access control list rules on the item’s parent item, reported by `stat()`.
- **`stat_physical_size`**: An integer that’s the physical size of the item on disk, reported by `stat()`.
- **`stat_resource_fork_size`**: An integer that’s the size of the item’s resource fork, reported by `stat()`.
- **`stat_uid`**: An integer that’s the user ID of the account that owns the item, reported by `stat()`.
- **`superpendingseterrors`**: An array containing the domain and code of the 5 most frequently encountered errors in the super pending set.
- **`superpendingsetsize`**: An integer that’s the number of items that haven’t been in sync for at least 1 minute.
- **`sys_is_docid_resolution_ok`**: An integer that indicates whether resolving the document ID of the documents returns the file ID of the item.
- **`sys_page_size`**: An integer that’s the system’s memory-page size, in bytes.
- **`sys_read_errno`**: An integer that’s the error number the system receives when it attemps to read the item.
- **`sys_uid`**: An integer that’s the user ID of the account that owns the item’s domain.
- **`xattr_compression_type`**: An integer that’s the item’s APFS compression type.
- **`xattr_count`**: An integer that’s the number of extended attributes on the item.
- **`xattr_has_before_bounce`**: An integer that indicates whether the item is renamed with a suffix because of a name collision.
- **`xattr_has_bundle_bit`**: An integer that indicates whether the item has the bundle bit set.
- **`xattr_has_demotion`**: An integer that indicates whether the item is a directory and has a flag to indicate that it shouldn’t be treated as a package.
- **`db_transfer_underlying_error_domain`**: A string that’s the domain of underlying error of the item’s latest transfer error. If there is no underlying error, this field isn’t set.
- **`db_transfer_underlying_error_code`**: An integer that’s the code of the underlying error of the item’s latest transfer error.
- **`disk_versus_fs_snapshot_diffs_in_pinned_folder_but_not_marked_accordingly`**: A Boolean that’s `true` if the item is a pinned folder with the corresponding extended attribute, but that this information isn’t propagated to the records for all descendent items; otherwise, it’s `false`.
- **`disk_versus_fs_snapshot_diffs_marked_in_pinned_folder_but_not_in_pinned_folder`**: A Boolean that’s `true` if the item isn’t in a pinned folder but its database record says that it is; otherwise, it’s `false`.

##### Understand the Character Set Bit Masks

The bits in the `name_characters_sets` bitfield are set to `1` when the following conditions are true, with bit `0` being the least significant bit:

- **`0`**: The item’s name contains one or more characters from [`controlCharacters`](https://developer.apple.com/documentation/foundation/nscharacterset/controlcharacters).
- **`1`**: The item’s name contains one or more characters from [`illegalCharacters`](https://developer.apple.com/documentation/foundation/nscharacterset/illegalcharacters).
- **`2`**: The item’s name contains one or more characters from [`nonBaseCharacters`](https://developer.apple.com/documentation/foundation/nscharacterset/nonbasecharacters).
- **`3`**: The item’s name contains one or more characters from [`symbols`](https://developer.apple.com/documentation/foundation/nscharacterset/symbols).
- **`4`**: The item’s name contains one or more emoji.
- **`5`**: The item’s name contains one or more characters that are outside the set `NSCharacterSet(range:NSMakeRange(0x0000, 0x024F))`; that is, characters that aren’t in the Base Latin, Latin-1, Extended Latin A or Extended Latin B sets.

##### Understand the Disconnection States

The `disconnection_state` field in the usage report enumerates the reason that file provider is disconnected. The possible values are:

- **`0`**: The file provider extension is connected and working.
- **`1`**: File provider is unable to start due to an error encountered by the recovery mechanism.
- **`2`**: The file provider domain is temporarily offline, for example, to apply an update.
- **`3`**: The file provider domain is permanently offline, for example, because someone logged out.
- **`4`**: File provider is unable to start because the system can’t find the file provider extension for the domain.
- **`5`**: File provider is unable to start because the device is low on disk space.
- **`6`**: File provider is unable to start because the domain’s database has a date in the future and the domain is on a non-default volume.
- **`7`**: File provider is unable to start because a mobile device management profile stops the system from using the file provider extension.
- **`8`**: File provider is unable to start because the domain is backed by an external drive and the provider rejected the domain.

##### Understand the Transfer Operation Types and Operation Reasons

The `db_transfer_operation_type` field in the consistency report’s erroneous item breakdown enumerates the operation type that encountered an error. The possible values are:

- **`1`**: Create an item.
- **`3`**: Update an item.
- **`4`**: Delete an item.
- **`5`**: Fetch an item’s metadata.
- **`6`**: Delete an empty folder from the snapshot.
- **`7`**: Regenerate the snapshot of an item’s children.
- **`8`**: Fetch the metadata of an item’s children.
- **`9`**: Materialize an item.
- **`10`**: Evict an item.
- **`11`**: Evict an item’s children.
- **`12`**: Rename an item with a suffix because of a name collision.
- **`13`**: Collect captured content.
- **`15`**: Delete a rejected item from the tree.
- **`16`**: Mark the disk import of a directory as done.
- **`17`**: Fault a directory in the tree.
- **`18`**: Cancel fetching a file’s content.
- **`19`**: Complete an import from disk.
- **`20`**: Continue an import from disk.
- **`21`**: Unfault a directory in the tree.
- **`22`**: Unfault a directory and its children.
- **`23`**: Merge items.
- **`24`**: Materialize a parent hierarchy.
- **`25`**: Cancel an update.
- **`26`**: Fetch an item’s content.
- **`27`**: Fetch an event stream.
- **`28`**: Materialize an ignored item.
- **`29`**: Unblock an item’s evictability.
- **`30`**: Mark packages as evictable.
- **`31`**: Mark packages as synchronization roots.
- **`32`**: Unblock ignoring processing for a folder.
- **`33`**: Ignore items that are children of an ignored folder hierarchy.
- **`34`**: Mark directories as locked.
- **`35`**: Complete a deferred rescan.
- **`36`**: Mark the item’s parent as deleted.
- **`37`**: Resume reconciliation.
- **`38`**: Retrigger resolved vendor exclusion.
- **`39`**: Resolve an item’s evictability.
- **`40`**: Populate conflicts.
- **`41`**: Clean remote versions.
- **`42`**: Update the item’s closest synchronization root.
- **`43`**: Rescan the parent of deleted children.
- **`44`**: Unblock item rejection.
- **`45`**: Unblock importing items from disk.
- **`46`**: Rescan the pending set on the filesystem side.
- **`47`**: Rescan the pending set on the file provider side.
- **`48`**: Unblock remote deletions.
- **`49`**: Unblock path-matching cycles.
- **`50`**: Unblock deletion of child items.
- **`1000`**: Rescan the generational store for unresolved conflicts.
- **`1001`**: Unmark a parent item as deleted when merging the source.
- **`1002`**: Re-import missing jobs.
- **`1003`**: Unblock path matching during import.
- **`1004`**: Unblock throttled reconciliations.
- **`1005`**: Unblock throttled item jobs.
- **`1006`**: Unblock throttled jobs.
- **`2000`**: Track a temporary item.
- **`2001`**: Rescan speculative items that are materialized and not fulfilled.
- **`2002`**: Materialize the parent hierarchy in the background.
- **`2003`**: Reimport a git repository or folder package.
- **`2004`**: Fix an out-of-sync base version on the filesystem.
- **`2005`**: Remove a stale conflict record that’s stored on disk.
- **`2006`**: Remove conflicting records of dataless items from the generational store.
- **`3500`**: Deletion acknowledged for an item.

The `reason` field in usage reports is a bitfield that enumerates the reasons the system performed the reported operation. The meaning of each bit in the bitfield, where bit `0` is the least-significant bit and bit `36` is the most-significant bit, are:

- **`0`**: The system materialized a file.
- **`1`**: The system evicted an item.
- **`2`**: The system created a folder in the tree.
- **`3`**: The system deleted a folder in the tree.
- **`4`**: The system was removing an empty folder and discovered that it wasn’t empty.
- **`5`**: The system rejected creation of an item.
- **`6`**: The system detected a conflict when it created an item.
- **`7`**: The system rejected an update of an item.
- **`8`**: The system detected a conflict when it updated an item.
- **`9`**: The system revived a deleted item.
- **`10`**: The system deleted an item in the tree.
- **`11`**: The system changed an item in the tree.
- **`12`**: The system detected that an item had been changed remotely.
- **`13`**: The system detected that an item changed while the system was fetching its content.
- **`14`**: The system collected garbage.
- **`15`**: The system’s stream reset.
- **`16`**: The system imported content from disk.
- **`17`**: Importing content from the disk completed.
- **`18`**: Importing content from the disk failed.
- **`19`**: The system cancelled an item’s materialization.
- **`21`**: The system detected that an item may already exist.
- **`22`**: The system merged multiple items.
- **`23`**: Someone requested the operation.
- **`24`**: The system performed work in the background.
- **`25`**: The system marked an item as ignored.
- **`26`**: The system marked an item as unignored.
- **`27`**: The system updated the item’s content.
- **`28`**: The system detected that the item on disk was dataless.
- **`29`**: The system changed the content policy.
- **`30`**: The system marked an item as ignored during disk import.
- **`31`**: The system detected that a deleted item was moved back in.
- **`32`**: The system renamed a source item to include a suffix because it detected a name conflict with an incoming item and couldn’t fetch the incoming item.
- **`33`**: The system checked if a disk import was complete.
- **`34`**: The system speculatively materialized an item.
- **`35`**: The system saved an temporary item while it resolved a conflict.
- **`36`**: The system re-evaluated the purgeability status of a new synchronization root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/exporting-file-provider-metrics-data)*