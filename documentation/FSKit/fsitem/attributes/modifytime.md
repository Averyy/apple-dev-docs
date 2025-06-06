# modifyTime

**Framework**: FSKit  
**Kind**: property

The item’s last-modified time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var modifyTime: timespec { get set }
```

#### Discussion

This property represents `mtime`, the last time the item’s contents changed.

## See Also

- [var accessTime: timespec](fsitem/attributes/accesstime.md)
  The item’s last-accessed time.
- [var changeTime: timespec](fsitem/attributes/changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](fsitem/attributes/birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](fsitem/attributes/backuptime.md)
  The item’s last-backup time.
- [var addedTime: timespec](fsitem/attributes/addedtime.md)
  The item’s added time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/modifytime)*