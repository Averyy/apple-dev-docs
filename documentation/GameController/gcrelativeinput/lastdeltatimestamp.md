# lastDeltaTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A timestamp for when the profile reports the delta value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastDeltaTimestamp: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval lastDeltaTimestamp;
```

## Discussion

This property isn’t a specific date and time. To determine the time between delta values, subtract a previous value from the current value.

## See Also

### Getting the delta value and timestamp
- [var delta: Float](./delta.md)
  The most recent amount of change in values that the profile records.
- [var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)?](./deltadidchangehandler.md)
  The block that the profile calls when the element’s input changes.
- [var lastDeltaLatency: TimeInterval](./lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/lastdeltatimestamp)*