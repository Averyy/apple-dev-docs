# supportsActiveJournal

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume currently uses a journal for speeding recovery after an unplanned shutdown.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsActiveJournal: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsActiveJournal;
```

## See Also

### Declaring journaling capabilities
- [var supportsJournal: Bool](./supportsjournal.md)
  A Boolean property that indicates whether the volume supports a journal used to speed recovery in case of unplanned restart, such as a power outage or crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsactivejournal)*