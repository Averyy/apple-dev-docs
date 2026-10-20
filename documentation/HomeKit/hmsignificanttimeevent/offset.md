# offset

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The offset from the significant event that the event fires at.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var offset: DateComponents? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDateComponents * offset;
```

## See Also

### Inspecting a significant time event
- [var significantEvent: HMSignificantEvent](./significantevent.md)
  The significant time-based event that is used to calculate when the event fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmsignificanttimeevent/offset)*