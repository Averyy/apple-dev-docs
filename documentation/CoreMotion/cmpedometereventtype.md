# CMPedometerEventType

**Framework**: Core Motion  
**Kind**: enum

Constants indicating the change that occurred to the user’s pedestrian activity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum CMPedometerEventType
```

## Topics

### Enumeration Cases
- [CMPedometerEventType.pause](cmpedometereventtype/pause.md)
  The user’s pedestrian activity stopped.
- [CMPedometerEventType.resume](cmpedometereventtype/resume.md)
  The user’s pedestrian activity resumed.
### Initializers
- [init?(rawValue: Int)](cmpedometereventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var date: Date](cmpedometerevent/date.md)
  The date on which the pedometer event was recorded.
- [var type: CMPedometerEventType](cmpedometerevent/type.md)
  The type of change that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometereventtype)*