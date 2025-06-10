# URLFileProtection

**Framework**: Foundation  
**Kind**: struct

Protection-level values for a URL resource key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URLFileProtection
```

#### Overview

These are values for the [`URLResourceKey`](urlresourcekey.md) key [`fileProtectionKey`](urlresourcekey/fileprotectionkey.md).

## Topics

### Creating a URL File Protection Type
- [init(rawValue: String)](urlfileprotection/init(rawvalue:).md)
  Creates a URL file protection type value.
### Protection levels
- [static let complete: URLFileProtection](urlfileprotection/complete.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [static let completeUnlessOpen: URLFileProtection](urlfileprotection/completeunlessopen.md)
  An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [static let completeUntilFirstUserAuthentication: URLFileProtection](urlfileprotection/completeuntilfirstuserauthentication.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [static let completeWhenUserInactive: URLFileProtection](urlfileprotection/completewhenuserinactive.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
- [static let none: URLFileProtection](urlfileprotection/none.md)
  An option that indicates the file has no special protections associated with it.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlfileprotection)*