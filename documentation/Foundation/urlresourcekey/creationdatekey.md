# creationDateKey

**Framework**: Foundation  
**Kind**: property

The time at which the resource was created.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let creationDateKey: URLResourceKey
```

#### Discussion

This key corresponds to an [`NSDate`](nsdate.md) value, or `nil` if the volume doesn’t support creation dates.

The corresponding resource is read-write.

A resource’s [`creationDateKey`](urlresourcekey/creationdatekey.md) value should be less than or equal to the resource’s [`contentModificationDateKey`](urlresourcekey/contentmodificationdatekey.md) and [`contentAccessDateKey`](urlresourcekey/contentaccessdatekey.md) values. Otherwise, the file system may change the [`creationDateKey`](urlresourcekey/creationdatekey.md) to the lesser of those values.

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

 This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

## See Also

- [static let keysOfUnsetValuesKey: URLResourceKey](urlresourcekey/keysofunsetvalueskey.md)
  Key for the resource properties that have not been set after the [`setResourceValues(_:)`](nsurl/setresourcevalues(_:).md) method returns an error, returned as an array of `NSString` objects.
- [static let quarantinePropertiesKey: URLResourceKey](urlresourcekey/quarantinepropertieskey.md)
- [static let addedToDirectoryDateKey: URLResourceKey](urlresourcekey/addedtodirectorydatekey.md)
  The time at which the resource’s was created or renamed into or within its parent directory, returned as an `NSDate`. Inconsistent behavior may be observed when this attribute is requested on hard-linked items. This property is not supported by all volumes. (read-only)
- [static let attributeModificationDateKey: URLResourceKey](urlresourcekey/attributemodificationdatekey.md)
  The time at which the resource’s attributes were most recently modified, returned as an `NSDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported (read-only).
- [static let contentAccessDateKey: URLResourceKey](urlresourcekey/contentaccessdatekey.md)
  The time at which the resource was most recently accessed.
- [static let contentModificationDateKey: URLResourceKey](urlresourcekey/contentmodificationdatekey.md)
  The time at which the resource was most recently modified.
- [static let customIconKey: URLResourceKey](urlresourcekey/customiconkey.md)
  The icon stored with the resource, returned as an `NSImage` object, or `nil` if the resource has no custom icon.
- [static let documentIdentifierKey: URLResourceKey](urlresourcekey/documentidentifierkey.md)
  The document identifier returned as an `NSNumber` (read-only).
- [static let effectiveIconKey: URLResourceKey](urlresourcekey/effectiveiconkey.md)
  The resource’s normal icon, returned as an `NSImage` object (read-only).
- [static let generationIdentifierKey: URLResourceKey](urlresourcekey/generationidentifierkey.md)
  An opaque generation identifier, returned as an `id <NSCopying, NSCoding, NSObject>` (read-only)
- [static let hasHiddenExtensionKey: URLResourceKey](urlresourcekey/hashiddenextensionkey.md)
  Key for determining whether the resource’s extension is normally removed from its localized name, returned as a Boolean `NSNumber` object (read-write).
- [static let isExcludedFromBackupKey: URLResourceKey](urlresourcekey/isexcludedfrombackupkey.md)
  A key for indicating whether the system excludes the resource from all backups of app data.
- [static let isExecutableKey: URLResourceKey](urlresourcekey/isexecutablekey.md)
  Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [static let isHiddenKey: URLResourceKey](urlresourcekey/ishiddenkey.md)
  Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
- [static let isReadableKey: URLResourceKey](urlresourcekey/isreadablekey.md)
  Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a Boolean `NSNumber` object (read-only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/creationdatekey)*