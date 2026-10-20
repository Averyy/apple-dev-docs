# addedTime

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The item’s added time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var addedTime: timespec { get set }
```

```objc
@property (nonatomic) struct timespec addedTime;
```

#### Discussion

This property represents the time the file system added the item to its parent directory.

## See Also

### Working with time attributes
- [var accessTime: timespec](./accesstime.md)
  The item’s last-accessed time.
- [var modifyTime: timespec](./modifytime.md)
  The item’s last-modified time.
- [var changeTime: timespec](./changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](./birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](./backuptime.md)
  The item’s last-backup time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/addedtime)*