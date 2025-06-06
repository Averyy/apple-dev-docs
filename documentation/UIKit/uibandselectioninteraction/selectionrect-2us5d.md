# selectionRect

**Framework**: UIKit  
**Kind**: property

The selection rectangle for an in-progress interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var selectionRect: CGRect? { get }
```

#### Discussion

The rectangle is in the coordinate system of the view that owns the interaction object. If no interaction is active, the value of this propety is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/selectionrect-2us5d)*