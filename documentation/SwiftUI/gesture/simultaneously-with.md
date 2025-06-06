# simultaneously(with:)

**Framework**: SwiftUI  
**Kind**: method

Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.

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
@preconcurrency func simultaneously<Other>(with other: Other) -> SimultaneousGesture<Self, Other> where Other : Gesture
```

#### Return Value

A gesture with two simultaneous gestures.

## Parameters

- `other`: A gesture that you want to combine with your gesture   to create a new, combined gesture.

## See Also

- [func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>](gesture/sequenced(before:).md)
  Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
- [func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>](gesture/exclusively(before:).md)
  Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/simultaneously(with:))*