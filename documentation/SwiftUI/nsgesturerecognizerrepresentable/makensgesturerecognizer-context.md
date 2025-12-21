# makeNSGestureRecognizer(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates an instance of the represented gesture recognizer.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeNSGestureRecognizer(context: Self.Context) -> Self.NSGestureRecognizerType
```

#### Discussion

> **Note**: Gesture recognizers are created on-demand and torn down when an event sequence ends, so do not perform expensive work in this method.

## Parameters

- `context`: A context structure containing information about   the current state of the system, such as the current coordinator   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/makensgesturerecognizer(context:))*