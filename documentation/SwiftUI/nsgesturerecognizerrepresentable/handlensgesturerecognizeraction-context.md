# handleNSGestureRecognizerAction(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Handles recognition of the represented `NSGestureRecognizer`.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func handleNSGestureRecognizerAction(_ recognizer: Self.NSGestureRecognizerType, context: Self.Context)
```

#### Discussion

If you implement this method, SwiftUI calls it when the wrapped gesture recognizer is recognized.

## Parameters

- `recognizer`: An instance of the represented gesture   recognizer.
- `context`: A context structure containing information about   the current state of the system, such as the current coordinator   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/handlensgesturerecognizeraction(_:context:))*