# FileProtectionType

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Protection level values that can be associated with a file attribute key.

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
struct FileProtectionType
```

```c
typedef NSString * NSFileProtectionType;
```

## Overview

These values are associated with the [`protectionKey`](./fileattributekey/protectionkey.md) key.

## Topics

### Creating a File Protection Type
- [init(rawValue: String)](./fileprotectiontype/init%28rawvalue%29.md)
  Creates a file protection type value.
### Working with Protection Levels
- [static let complete: FileProtectionType](./fileprotectiontype/complete.md)
  The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [static let completeUnlessOpen: FileProtectionType](./fileprotectiontype/completeunlessopen.md)
  The file is stored in an encrypted format on disk after it is closed.
- [static let completeUntilFirstUserAuthentication: FileProtectionType](./fileprotectiontype/completeuntilfirstuserauthentication.md)
  The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [static let none: FileProtectionType](./fileprotectiontype/none.md)
  The file has no special protections associated with it.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [FileManager.DirectoryEnumerationOptions](./filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](./filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](./filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](./fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](./fileattributetype.md)
  Values representing a file’s type attribute.
- [struct URLFileProtection](./urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileprotectiontype)*