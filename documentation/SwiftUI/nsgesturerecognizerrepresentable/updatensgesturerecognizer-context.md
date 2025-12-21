# updateNSGestureRecognizer(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the `NSGestureRecognizer` (and coordinator) to the latest configuration.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateNSGestureRecognizer(_ recognizer: Self.NSGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer`: An instance of the represented gesture   recognizer.
- `context`: A context structure containing information about   the current state of the system, such as the current coordinator   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/updatensgesturerecognizer(_:context:))*