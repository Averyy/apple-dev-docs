# updateUIGestureRecognizer(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the `UIGestureRecognizer` (and coordinator) to the latest configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateUIGestureRecognizer(_ recognizer: Self.UIGestureRecognizerType, context: Self.Context)
```

## Parameters

- `recognizer`: An instance of the represented gesture   recognizer.
- `context`: A context structure containing information about   the current state of the system, such as the current coordinator   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/updateuigesturerecognizer(_:context:))*