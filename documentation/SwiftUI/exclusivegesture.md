# ExclusiveGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that consists of two gestures where only one of them can succeed.

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
struct ExclusiveGesture<First, Second> where First : Gesture, Second : Gesture
```

#### Overview

The `ExclusiveGesture` gives precedence to its first gesture.

## Topics

### Creating the gesture
- [init(First, Second)](exclusivegesture/init(_:_:).md)
  Creates a gesture from two gestures where only one of them succeeds.
- [var first: First](exclusivegesture/first.md)
  The first of two gestures.
- [var second: Second](exclusivegesture/second.md)
  The second of two gestures.
### Supporting types
- [ExclusiveGesture.Value](exclusivegesture/value.md)
  The value of an exclusive gesture that indicates which of two gestures succeeded.

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
- [struct SequenceGesture](sequencegesture.md)
  A gesture that’s a sequence of two gestures.
- [struct SimultaneousGesture](simultaneousgesture.md)
  A gesture containing two gestures that can happen at the same time with neither of them preceding the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/exclusivegesture)*