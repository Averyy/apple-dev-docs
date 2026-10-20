# backupTime

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The item’s last-backup time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var backupTime: timespec { get set }
```

```objc
@property (nonatomic) struct timespec backupTime;
```

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
- [var addedTime: timespec](./addedtime.md)
  The item’s added time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/backuptime)*