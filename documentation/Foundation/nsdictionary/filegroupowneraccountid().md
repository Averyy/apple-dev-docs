# fileGroupOwnerAccountID()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns file’s group owner account ID.

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
func fileGroupOwnerAccountID() -> NSNumber?
```

```objc
- (NSNumber *) fileGroupOwnerAccountID;
```

#### Return Value

The value associated with the [`groupOwnerAccountID`](../fileattributekey/groupowneraccountid.md) file attributes key, or `nil` if the file attributes dictionary has no entry for the key.

## See Also

### Accessing File Attributes
- [func fileSize() -> UInt64](./filesize%28%29.md)
  Returns the file’s size, in bytes.
- [func fileType() -> String?](./filetype%28%29.md)
  Returns the file type.
- [func fileCreationDate() -> Date?](./filecreationdate%28%29.md)
  Returns the file’s creation date.
- [func fileModificationDate() -> Date?](./filemodificationdate%28%29.md)
  Returns file’s modification date.
- [func filePosixPermissions() -> Int](./fileposixpermissions%28%29.md)
  Returns the file’s POSIX permissions.
- [func fileOwnerAccountID() -> NSNumber?](./fileowneraccountid%28%29.md)
  Returns the file’s owner account ID.
- [func fileOwnerAccountName() -> String?](./fileowneraccountname%28%29.md)
  Returns the file’s owner account name.
- [func fileGroupOwnerAccountName() -> String?](./filegroupowneraccountname%28%29.md)
  Returns the file’s group owner account name.
- [func fileExtensionHidden() -> Bool](./fileextensionhidden%28%29.md)
  Returns a Boolean value indicating whether the file hides its extension.
- [func fileIsImmutable() -> Bool](./fileisimmutable%28%29.md)
  Returns a Boolean value indicating whether the file is immutable.
- [func fileIsAppendOnly() -> Bool](./fileisappendonly%28%29.md)
  Returns a Boolean value indicating whether the file is append only.
- [func fileSystemFileNumber() -> Int](./filesystemfilenumber%28%29.md)
  Returns the filesystem file number.
- [func fileSystemNumber() -> Int](./filesystemnumber%28%29.md)
  Returns the filesystem number.
- [func fileHFSTypeCode() -> OSType](./filehfstypecode%28%29.md)
  Returns file’s HFS type code.
- [func fileHFSCreatorCode() -> OSType](./filehfscreatorcode%28%29.md)
  Returns the file’s HFS creator code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/filegroupowneraccountid())*