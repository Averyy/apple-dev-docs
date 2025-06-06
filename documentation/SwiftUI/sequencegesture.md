# SequenceGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that’s a sequence of two gestures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct SequenceGesture<First, Second> where First : Gesture, Second : Gesture
```

#### Overview

Read [`Composing SwiftUI gestures`](composing-swiftui-gestures.md) to learn how you can create a sequence of two gestures.

## Topics

### Creating the gesture
- [init(First, Second)](sequencegesture/init(_:_:).md)
  Creates a sequence gesture with two gestures.
- [var first: First](sequencegesture/first.md)
  The first gesture in a sequence of two gestures.
- [var second: Second](sequencegesture/second.md)
  The second gesture in a sequence of two gestures.
### Getting the gesture’s values
- [SequenceGesture.Value](sequencegesture/value.md)
  The value of a sequence gesture that helps to detect whether the first gesture succeeded, so the second gesture can start.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [Composing SwiftUI gestures](composing-swiftui-gestures.md)
  Combine gestures to create complex interactions.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](view/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](view/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [struct SimultaneousGesture](simultaneousgesture.md)
  A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [struct ExclusiveGesture](exclusivegesture.md)
  A gesture that consists of two gestures where only one of them can succeed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sequencegesture)*