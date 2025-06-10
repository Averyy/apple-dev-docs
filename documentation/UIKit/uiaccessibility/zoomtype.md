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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIAccessibilityContainer](uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [@MainActor var accessibilityActivationPoint: CGPoint { get set }](../ObjectiveC/NSObject-swift.class/accessibilityActivationPoint.md)
- [var accessibilityFocusedUIElement: Any? { get }](../ObjectiveC/NSObject-swift.class/accessibilityFocusedUIElement.md)
- [@MainActor var accessibilityFrame: CGRect { get set }](../ObjectiveC/NSObject-swift.class/accessibilityFrame.md)
- [func accessibilityHitTest(_ point: NSPoint) -> Any?](../ObjectiveC/NSObject-swift.class/accessibilityHitTest(_:).md)
- [@MainActor var accessibilityNavigationStyle: UIAccessibilityNavigationStyle { get set }](../ObjectiveC/NSObject-swift.class/accessibilityNavigationStyle.md)
- [enum UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md)
  Constants that describe how to navigate an object’s elements with an assistive app.
- [@MainActor @NSCopying var accessibilityPath: UIBezierPath? { get set }](../ObjectiveC/NSObject-swift.class/accessibilityPath.md)
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype)*