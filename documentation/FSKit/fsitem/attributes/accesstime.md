# accessTime

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The item’s last-accessed time.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var accessTime: timespec { get set }
```

```objc
@property (nonatomic) struct timespec accessTime;
```

## See Also

### Working with time attributes
- [var modifyTime: timespec](./modifytime.md)
  The item’s last-modified time.
- [var changeTime: timespec](./changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](./birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](./backuptime.md)
  The item’s last-backup time.
- [var addedTime: timespec](./addedtime.md)
  The item’s added time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/accesstime)*