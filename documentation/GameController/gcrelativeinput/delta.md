# delta

**Framework**: Game Controller  
**Kind**: property  
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

## See Also

- [var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)?](gcrelativeinput/deltadidchangehandler.md)
  The block that the profile calls when the element’s input changes.
- [var lastDeltaTimestamp: TimeInterval](gcrelativeinput/lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.
- [var lastDeltaLatency: TimeInterval](gcrelativeinput/lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/delta)*