# offset

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The offset from the significant event that this event fires at.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var offset: DateComponents { get set }
```

```objc
@property (nonatomic, strong, readwrite) NSDateComponents * offset;
```

#### Discussion

To specify that this event should fire before the significant event, supply a date components object with negative values. For example, to specify 30 minutes before sunset, the [`minute`](../../Foundation/datecomponents/minute.md) property of the value of the [`offset`](./offset.md) property must be set to `-30`.

## See Also

### Configuring a significant time event
- [var significantEvent: HMSignificantEvent](./significantevent.md)
  The significant time-based event that is used to calculate when the event fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablesignificanttimeevent/offset)*