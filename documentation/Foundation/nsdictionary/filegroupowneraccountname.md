# fileGroupOwnerAccountName()

**Framework**: Foundation  
**Kind**: method

Returns the file’s group owner account name.

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
func fileGroupOwnerAccountName() -> String?
```

#### Return Value

The value associated with the [`groupOwnerAccountName`](fileattributekey/groupowneraccountname.md) file attributes key, or `nil` if the file attributes dictionary has no entry for the key.

## See Also

- [func fileSize() -> UInt64](nsdictionary/filesize.md)
  Returns the file’s size, in bytes.
- [func fileType() -> String?](nsdictionary/filetype.md)
  Returns the file type.
- [func fileCreationDate() -> Date?](nsdictionary/filecreationdate.md)
  Returns the file’s creation date.
- [func fileModificationDate() -> Date?](nsdictionary/filemodificationdate.md)
  Returns file’s modification date.
- [func filePosixPermissions() -> Int](nsdictionary/fileposixpermissions.md)
  Returns the file’s POSIX permissions.
- [func fileOwnerAccountID() -> NSNumber?](nsdictionary/fileowneraccountid.md)
  Returns the file’s owner account ID.
- [func fileOwnerAccountName() -> String?](nsdictionary/fileowneraccountname.md)
  Returns the file’s owner account name.
- [func fileGroupOwnerAccountID() -> NSNumber?](nsdictionary/filegroupowneraccountid.md)
  Returns file’s group owner account ID.
- [func fileExtensionHidden() -> Bool](nsdictionary/fileextensionhidden.md)
  Returns a Boolean value indicating whether the file hides its extension.
- [func fileIsImmutable() -> Bool](nsdictionary/fileisimmutable.md)
  Returns a Boolean value indicating whether the file is immutable.
- [func fileIsAppendOnly() -> Bool](nsdictionary/fileisappendonly.md)
  Returns a Boolean value indicating whether the file is append only.
- [func fileSystemFileNumber() -> Int](nsdictionary/filesystemfilenumber.md)
  Returns the filesystem file number.
- [func fileSystemNumber() -> Int](nsdictionary/filesystemnumber.md)
  Returns the filesystem number.
- [func fileHFSTypeCode() -> OSType](nsdictionary/filehfstypecode.md)
  Returns file’s HFS type code.
- [func fileHFSCreatorCode() -> OSType](nsdictionary/filehfscreatorcode.md)
  Returns the file’s HFS creator code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/filegroupowneraccountname())*