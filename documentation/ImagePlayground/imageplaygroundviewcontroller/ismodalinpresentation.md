# isModalInPresentation

**Framework**: Image Playground  
**Kind**: property

A Boolean value indicating whether the view controller enforces a modal behavior.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var isModalInPresentation: Bool { get set }
```

#### Discussion

The view controller prevents swiping or tapping away its interface if there are active changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/ismodalinpresentation)*