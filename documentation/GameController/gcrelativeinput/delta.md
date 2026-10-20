# delta

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The most recent amount of change in values that the profile records.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var delta: Float { get }
```

```objc
@property (readonly) float delta;
```

## See Also

### Getting the delta value and timestamp
- [var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)?](./deltadidchangehandler.md)
  The block that the profile calls when the element’s input changes.
- [var lastDeltaTimestamp: TimeInterval](./lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.
- [var lastDeltaLatency: TimeInterval](./lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/delta)*