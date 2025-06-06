# SimultaneousGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture containing two gestures that can happen at the same time with neither of them preceding the other.

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
struct SimultaneousGesture<First, Second> where First : Gesture, Second : Gesture
```

#### Overview

A simultaneous gesture is a container-event handler that evaluates its two child gestures at the same time. Its value is a struct with two optional values, each representing the phases of one of the two gestures.

## Topics

### Creating the gesture
- [init(First, Second)](simultaneousgesture/init(_:_:).md)
  Creates a gesture with two gestures that can receive updates or succeed independently of each other.
- [var first: First](simultaneousgesture/first.md)
  The first of two gestures that can happen simultaneously.
- [var second: Second](simultaneousgesture/second.md)
  The second of two gestures that can happen simultaneously.
### Getting the gesture’s values
- [SimultaneousGesture.Value](simultaneousgesture/value.md)
  The value of a simultaneous gesture that indicates which of its two gestures receives events.

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
- [struct ExclusiveGesture](exclusivegesture.md)
  A gesture that consists of two gestures where only one of them can succeed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/simultaneousgesture)*