# init(_:)

**Framework**: Apple Archive  
**Kind**: init

Creates a new field key set from the specified comma-separated string of three-letter keys.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init?(_ s: String)
```

#### Discussion

Apple Archive supports the following three-letter keys:

- **`typ`**: The entry type (always included).
- **`pat`**: The entry path (always included for filesystem objects).
- **`lnk`**: The link path (always included for symbolic links).
- **`dev`**: The device id (always included for block and character devices).
- **`uid`**: The user id.
- **`gid`**: The group id.
- **`mod`**: The access mode.
- **`flg`**: The BSD flags.
- **`mtm`**: The modification time.
- **`btm`**: The backup time.
- **`ctm`**: The creation time.
- **`dat`**: The file data.
- **`siz`**: The file data size.
- **`cks`**: The file data digest (POSIX 1003.2-1992 32-bit CRC).
- **`sh1`**: The file data SHA-1 digest.
- **`sh2`**: The file data SHA-256 digest.
- **`sh3`**: The file data SHA-384 digest.
- **`sh5`**: The file data SHA-512 digest.
- **`xat`**: The extended attributes.
- **`acl`**: The access control list.
- **`duz`**: The entry disk usage.
- **`idx`**: The entry index in input archive.
- **`idz`**: The entry size in input archive.
- **`yec`**: The file data error correcting codes.
- **`yaf`**: The list of archive fields (metadata entry).

## Parameters

- `s`: The key set string representation.

## See Also

- [init()](archiveheader/fieldkeyset/init.md)
  Creates a new empty field key set.
- [init(copying: ArchiveHeader.FieldKeySet)](archiveheader/fieldkeyset/init(copying:).md)
  Creates a copy of the specified field key set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldkeyset/init(_:))*