# InferenceValue.NamedMutableViews

**Framework**: Core AI  
**Kind**: struct

A collection of named mutable views into inference values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NamedMutableViews
```

#### Overview

Each view can only be taken once to ensure exclusive access.

## Topics

### Accessing views
- [func take(String) -> InferenceValue.MutableView?](inferencevalue/namedmutableviews/take(_:).md)
  Takes the mutable view for the specified value.

## See Also

- [InferenceValue.View](inferencevalue/view.md)
  A borrowed, read-only view of an inference value.
- [InferenceValue.MutableView](inferencevalue/mutableview.md)
  A borrowed, mutable view of an inference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/namedmutableviews)*