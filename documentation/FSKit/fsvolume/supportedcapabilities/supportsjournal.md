# supportsJournal

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume supports a journal used to speed recovery in case of unplanned restart, such as a power outage or crash.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsJournal: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsJournal;
```

## Discussion

This property doesn’t necessarily mean the volume is actively using a journal.

## See Also

### Declaring journaling capabilities
- [var supportsActiveJournal: Bool](./supportsactivejournal.md)
  A Boolean property that indicates whether the volume currently uses a journal for speeding recovery after an unplanned shutdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsjournal)*