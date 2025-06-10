# renderHandler

**Framework**: PHASE  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var renderHandler: PHASEPullStreamRenderHandler { get set }
```

#### Discussion

The renderBlock must be set before the PHASESoundEvent is prepared or started.  The callback will be called from a high priority realtime thread. Your implementation must be performant and not perform any realtime unsafe operations such as lock mutexes or allocate memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepullstreamnode/renderhandler)*