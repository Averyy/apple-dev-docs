# init(relativeOffset:)

**Framework**: EventKit  
**Kind**: init

Creates and returns an alarm with a relative offset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(relativeOffset offset: TimeInterval)
```

#### Return Value

The created alarm.

#### Discussion

Negative offset values fire before the start of the event, while positive values fire after the start.

## Parameters

- `offset`: The offset from the start of an event, at which the alarm fires.

## See Also

- [init(absoluteDate: Date)](ekalarm/init(absolutedate:).md)
  Creates and returns an alarm with an absolute date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/init(relativeoffset:))*