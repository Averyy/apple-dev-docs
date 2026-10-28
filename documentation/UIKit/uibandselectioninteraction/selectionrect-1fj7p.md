# selectionRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The selection rectangle for an in-progress interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) CGRect selectionRect;
```

## Discussion

The rectangle is in the coordinate system of the view that owns the interaction object. If no interaction is active, the value of this propety is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/selectionrect-1fj7p)*