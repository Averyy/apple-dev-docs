# deltaDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The block that the profile calls when the element’s input changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)? { get set }
```

#### Discussion

The block’s parameters are:

## See Also

- [var delta: Float](gcrelativeinput/delta.md)
  The most recent amount of change in values that the profile records.
- [var lastDeltaTimestamp: TimeInterval](gcrelativeinput/lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.
- [var lastDeltaLatency: TimeInterval](gcrelativeinput/lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/deltadidchangehandler)*