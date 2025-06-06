# handleUIGestureRecognizerAction(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Handles recognition of the represented `UIGestureRecognizer`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func handleUIGestureRecognizerAction(_ recognizer: Self.UIGestureRecognizerType, context: Self.Context)
```

#### Discussion

If you implement this method, SwiftUI calls it when the wrapped gesture recognizer is recognized.

## Parameters

- `recognizer`: An instance of the represented gesture   recognizer.
- `context`: A context structure containing information about   the current state of the system, such as the current coordinator   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/handleuigesturerecognizeraction(_:context:))*