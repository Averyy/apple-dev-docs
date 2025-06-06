# kCFURLContentAccessDateKey

**Framework**: Core Foundation  
**Kind**: var

Key for the last time the resource was accessed, returned as a `CFDate` object if the volume supports access dates, or `nil` if access dates are unsupported.

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
let kCFURLContentAccessDateKey: CFString!
```

## See Also

- [let kCFURLNameKey: CFString!](kcfurlnamekey.md)
  Key for the resource’s name in the file system, returned as a `CFString` object.
- [let kCFURLLocalizedNameKey: CFString!](kcfurllocalizednamekey.md)
  Key for the resource’s localized or extension-hidden name, retuned as a `CFString` object.
- [let kCFURLPathKey: CFString!](kcfurlpathkey.md)
  A `CFString` value containing the URL’s path as a file system path. (read-only)
- [let kCFURLIsRegularFileKey: CFString!](kcfurlisregularfilekey.md)
  Key for determining whether the resource is a regular file, as opposed to a directory or a symbolic link. Returned as a `CFBoolean` object.
- [let kCFURLIsDirectoryKey: CFString!](kcfurlisdirectorykey.md)
  Key for determining whether the resource is a directory, returned as a `CFBoolean` object.
- [let kCFURLIsSymbolicLinkKey: CFString!](kcfurlissymboliclinkkey.md)
  Key for determining whether the resource is a symbolic link, returned as a `CFBoolean` object.
- [let kCFURLIsVolumeKey: CFString!](kcfurlisvolumekey.md)
  Key for determining whether the resource is the root directory of a volume, returned as a `CFBoolean` object.
- [let kCFURLIsPackageKey: CFString!](kcfurlispackagekey.md)
  Key for determining whether the resource is a packaged directory, returned as a `CFBoolean` object.
- [let kCFURLIsSystemImmutableKey: CFString!](kcfurlissystemimmutablekey.md)
  Key for determining whether the resource’s system immutable bit is set, returned as a `CFBoolean` object.
- [let kCFURLIsUserImmutableKey: CFString!](kcfurlisuserimmutablekey.md)
  Key for determining whether the resource’s user immutable bit is set, returned as a `CFBoolean` object.
- [let kCFURLIsHiddenKey: CFString!](kcfurlishiddenkey.md)
  Key for determining whether the resource is normally not displayed to users, returned as a `CFBoolean` object.
- [let kCFURLHasHiddenExtensionKey: CFString!](kcfurlhashiddenextensionkey.md)
  Key for determining whether the resource’s extension is normally removed from its localized name, returned as a `CFBoolean` object.
- [let kCFURLCreationDateKey: CFString!](kcfurlcreationdatekey.md)
  Key for the resource’s creation date, returned as a `CFDate` object if the volume supports creation dates, or `nil` if creation dates are unsupported.
- [let kCFURLContentModificationDateKey: CFString!](kcfurlcontentmodificationdatekey.md)
  Key for the last time the resource was modified, returned as a `CFDate` object if the volume supports modification dates, or `nil` if modification dates are unsupported.
- [let kCFURLAttributeModificationDateKey: CFString!](kcfurlattributemodificationdatekey.md)
  Key for the last time the resource’s attributes were modified, returned as a `CFDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlcontentaccessdatekey)*