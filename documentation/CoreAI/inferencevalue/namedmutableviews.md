# InferenceValue.NamedMutableViews

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A collection of named mutable views into inference values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct NamedMutableViews
```

#### Overview

Each view can only be taken once to ensure exclusive access.

## Topics

### Accessing views
- [func take(String) -> InferenceValue.MutableView?](./namedmutableviews/take%28_%29.md)
  Takes the mutable view for the specified value.

## See Also

### Accessing views
- [InferenceValue.View](./view.md)
  A borrowed, read-only view of an inference value.
- [InferenceValue.MutableView](./mutableview.md)
  A borrowed, mutable view of an inference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/namedmutableviews)*