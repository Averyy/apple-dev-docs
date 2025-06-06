# sequenced(before:)

**Framework**: SwiftUI  
**Kind**: method

Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.

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
@MainActor
@preconcurrency func sequenced<Other>(before other: Other) -> SequenceGesture<Self, Other> where Other : Gesture
```

#### Return Value

A gesture that’s a sequence of two gestures.

## Parameters

- `other`: A gesture you want to combine with another gesture to   create a new, sequenced gesture.

## See Also

- [func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>](gesture/simultaneously(with:).md)
  Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>](gesture/exclusively(before:).md)
  Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/sequenced(before:))*