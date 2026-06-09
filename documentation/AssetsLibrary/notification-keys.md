# Notification Keys

**Framework**: Assets Library

Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.

#### Overview

Assets that are modified use the [`ALAssetLibraryUpdatedAssetsKey`](alassetlibraryupdatedassetskey.md) key. Assets that are inserted or deleted use the [`ALAssetLibraryUpdatedAssetGroupsKey`](alassetlibraryupdatedassetgroupskey.md) key for the asset group that contains the asset.

Assets and asset groups that have no strong references are omitted from the notification’s user information dictionary.

## See Also

- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/notification-keys)*