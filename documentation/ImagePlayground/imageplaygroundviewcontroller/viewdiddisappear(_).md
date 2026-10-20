# viewDidDisappear(_:)

**Framework**: Image Playground  
**Kind**: method

Notifies the view controller that its view is about to be removed from a view hierarchy.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func viewDidDisappear(_ animated: Bool)
```

#### Discussion

The view controller uses this method to remove its interface configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/viewdiddisappear(_:))*