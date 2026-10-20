# MTRSetMessageReliabilityParameters(_:_:_:_:)

**Framework**: Matter  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
func MTRSetMessageReliabilityParameters(_ idleRetransmitMs: NSNumber?, _ activeRetransmitMs: NSNumber?, _ activeThresholdMs: NSNumber?, _ additionalRetransmitDelayMs: NSNumber?)
```

```c
extern void MTRSetMessageReliabilityParameters(NSNumber *idleRetransmitMs, NSNumber *activeRetransmitMs, NSNumber *activeThresholdMs, NSNumber *additionalRetransmitDelayMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrsetmessagereliabilityparameters(_:_:_:_:))*