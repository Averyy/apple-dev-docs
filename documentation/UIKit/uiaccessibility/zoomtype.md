# UIAccessibility.ZoomType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The types of system Zoom that can be in effect.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum ZoomType
```

```c
enum UIAccessibilityZoomType : NSInteger;
```

## Topics

### Constants
- [UIAccessibility.ZoomType.insertionPoint](./zoomtype/insertionpoint.md)
  The system zoom type is the text insertion point.
### Initializers
- [init?(rawValue: Int)](./zoomtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Navigating elements
- [UIAccessibilityContainer](../uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [var accessibilityActivationPoint: CGPoint](../../ObjectiveC/nsobject-swift.class/accessibilityactivationpoint.md)
- [var accessibilityFocusedUIElement: Any?](../../ObjectiveC/nsobject-swift.class/accessibilityfocuseduielement.md)
- [var accessibilityFrame: CGRect](../../ObjectiveC/nsobject-swift.class/accessibilityframe.md)
- [func accessibilityHitTest(NSPoint) -> Any?](../../ObjectiveC/nsobject-swift.class/accessibilityhittest%28_%29.md)
- [var accessibilityNavigationStyle: UIAccessibilityNavigationStyle](../../ObjectiveC/nsobject-swift.class/accessibilitynavigationstyle.md)
- [enum UIAccessibilityNavigationStyle](../uiaccessibilitynavigationstyle.md)
  Constants that describe how to navigate an object’s elements with an assistive app.
- [var accessibilityPath: UIBezierPath?](../../ObjectiveC/nsobject-swift.class/accessibilitypath.md)
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](./zoomfocuschanged%28zoomtype,toframe,in%29.md)
  Notifies the system when the app’s focus changes to a new location.
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](../uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype)*