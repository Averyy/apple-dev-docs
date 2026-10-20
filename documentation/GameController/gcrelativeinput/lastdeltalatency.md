# lastDeltaLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The time in seconds between the current and the previous delta values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastDeltaLatency: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval lastDeltaLatency;
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

### Getting the delta value and timestamp
- [var delta: Float](./delta.md)
  The most recent amount of change in values that the profile records.
- [var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)?](./deltadidchangehandler.md)
  The block that the profile calls when the element’s input changes.
- [var lastDeltaTimestamp: TimeInterval](./lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/lastdeltalatency)*