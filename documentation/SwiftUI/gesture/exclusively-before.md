# exclusively(before:)

**Framework**: SwiftUI  
**Kind**: method

Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.

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
nonisolated
func exclusively<Other>(before other: Other) -> ExclusiveGesture<Self, Other> where Other : Gesture
```

#### Return Value

A gesture that’s the result of combining two gestures where only one of them can succeed. SwiftUI gives precedence to the first gesture.

## Parameters

- `other`: A gesture you combine with your gesture, to create a   new, combined gesture.

## See Also

- [func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>](gesture/simultaneously(with:).md)
  Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>](gesture/sequenced(before:).md)
  Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/exclusively(before:))*