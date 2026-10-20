# InferenceValue.View

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A borrowed, read-only view of an inference value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct View
```

#### Overview

Use views to pass input values to [`InferenceFunction.Inputs`](../inferencefunction/inputs.md) without transferring ownership.

## See Also

### Accessing views
- [InferenceValue.MutableView](./mutableview.md)
  A borrowed, mutable view of an inference value.
- [InferenceValue.NamedMutableViews](./namedmutableviews.md)
  A collection of named mutable views into inference values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/view)*