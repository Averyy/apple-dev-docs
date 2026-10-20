# deltaDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (atomic, copy, nullable) void (^deltaDidChangeHandler)(id<GCPhysicalInputElement>element, id<GCRelativeInput>input, float delta);
```

#### Discussion

The block’s parameters are:

- **`element`**: The element whose input changes.
- **`input`**: The input object that represents the relative or delta value.
- **`delta`**: The amount that the input changed since the last time the profile called this block.

## See Also

### Getting the delta value and timestamp
- [var delta: Float](./delta.md)
  The most recent amount of change in values that the profile records.
- [var lastDeltaTimestamp: TimeInterval](./lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.
- [var lastDeltaLatency: TimeInterval](./lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput/deltadidchangehandler)*