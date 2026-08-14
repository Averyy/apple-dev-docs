# UIAccessibility.ZoomType

**Framework**: UIKit  
**Kind**: enum

The types of system Zoom that can be in effect.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum ZoomType
```

## Topics

### Constants
- [UIAccessibility.ZoomType.insertionPoint](uiaccessibility/zoomtype/insertionpoint.md)
  The system zoom type is the text insertion point.
### Initializers
- [init?(rawValue: Int)](uiaccessibility/zoomtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [UIAccessibilityContainer](uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [var accessibilityActivationPoint: CGPoint](../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [var accessibilityFocusedUIElement: Any?](../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [var accessibilityFrame: CGRect](../objectivec/nsobject-swift.class/accessibilityframe.md)
- [func accessibilityHitTest(NSPoint) -> Any?](../objectivec/nsobject-swift.class/accessibilityhittest(_:).md)
- [var accessibilityNavigationStyle: UIAccessibilityNavigationStyle](../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [enum UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md)
  Constants that describe how to navigate an object’s elements with an assistive app.
- [var accessibilityPath: UIBezierPath?](../objectivec/nsobject-swift.class/accessibilitypath.md)
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype)*