# FileAttributeType

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Values representing a file’s type attribute.

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
struct FileAttributeType
```

```c
typedef NSString * NSFileAttributeType;
```

#### Discussion

These strings are the possible values for the [`type`](./fileattributekey/type.md) attribute key contained in the dictionary object returned by [`attributesOfItem(atPath:)`](./filemanager/attributesofitem%28atpath%29.md).

## Topics

### Creating a File Attribute Type
- [init(rawValue: String)](./fileattributetype/init%28rawvalue%29.md)
  Creates a file attribute type value.
### Accessing File Type Attributes
- [static let typeBlockSpecial: FileAttributeType](./fileattributetype/typeblockspecial.md)
  A block special file.
- [static let typeCharacterSpecial: FileAttributeType](./fileattributetype/typecharacterspecial.md)
  A character special file.
- [static let typeDirectory: FileAttributeType](./fileattributetype/typedirectory.md)
  A directory.
- [static let typeRegular: FileAttributeType](./fileattributetype/typeregular.md)
  A regular file.
- [static let typeSocket: FileAttributeType](./fileattributetype/typesocket.md)
  A socket.
- [static let typeSymbolicLink: FileAttributeType](./fileattributetype/typesymboliclink.md)
  A symbolic link.
- [static let typeUnknown: FileAttributeType](./fileattributetype/typeunknown.md)
  A file whose type is unknown.

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
- [struct FileProtectionType](./fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](./urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileattributetype)*