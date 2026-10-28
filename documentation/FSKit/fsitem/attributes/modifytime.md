# modifyTime

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The item’s last-modified time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var modifyTime: timespec { get set }
```

```objc
@property (nonatomic) struct timespec modifyTime;
```

## Discussion

This property represents `mtime`, the last time the item’s contents changed.

## See Also

### Working with time attributes
- [var accessTime: timespec](./accesstime.md)
  The item’s last-accessed time.
- [var changeTime: timespec](./changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](./birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](./backuptime.md)
  The item’s last-backup time.
- [var addedTime: timespec](./addedtime.md)
  The item’s added time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/modifytime)*