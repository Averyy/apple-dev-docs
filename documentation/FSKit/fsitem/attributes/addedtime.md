# addedTime

**Framework**: FSKit  
**Kind**: property

The item’s added time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var addedTime: timespec { get set }
```

#### Discussion

This property represents the time the file system added the item to its parent directory.

## See Also

- [var accessTime: timespec](fsitem/attributes/accesstime.md)
  The item’s last-accessed time.
- [var modifyTime: timespec](fsitem/attributes/modifytime.md)
  The item’s last-modified time.
- [var changeTime: timespec](fsitem/attributes/changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](fsitem/attributes/birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](fsitem/attributes/backuptime.md)
  The item’s last-backup time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/addedtime)*