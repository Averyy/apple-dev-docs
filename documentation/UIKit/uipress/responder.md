# responder

**Framework**: UIKit  
**Kind**: property

A responder object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var responder: UIResponder? { get }
```

#### Discussion

This property is a [`UIResponder`](uiresponder.md) object that either is focused or is the [`isFirstResponder`](uiresponder/isfirstresponder.md) object in the window when [`UIApplication`](uiapplication.md) originally dispatched the press event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/responder)*