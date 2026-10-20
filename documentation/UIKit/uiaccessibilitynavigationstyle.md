# UIAccessibilityNavigationStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe how to navigate an object’s elements with an assistive app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum UIAccessibilityNavigationStyle
```

```c
enum UIAccessibilityNavigationStyle : NSInteger;
```

## Topics

### Constants
- [UIAccessibilityNavigationStyle.automatic](./uiaccessibilitynavigationstyle/automatic.md)
  The assistive technology automatically determines how the receiver’s elements should be navigated.
- [UIAccessibilityNavigationStyle.separate](./uiaccessibilitynavigationstyle/separate.md)
  The receiver’s elements should be navigated as separate elements.
- [UIAccessibilityNavigationStyle.combined](./uiaccessibilitynavigationstyle/combined.md)
  The receiver’s elements should be combined and navigated as a single item.
### Initializers
- [init?(rawValue: Int)](./uiaccessibilitynavigationstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Navigating elements
- [UIAccessibilityContainer](./uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [var accessibilityActivationPoint: CGPoint](../ObjectiveC/nsobject-swift.class/accessibilityactivationpoint.md)
- [var accessibilityFocusedUIElement: Any?](../ObjectiveC/nsobject-swift.class/accessibilityfocuseduielement.md)
- [var accessibilityFrame: CGRect](../ObjectiveC/nsobject-swift.class/accessibilityframe.md)
- [func accessibilityHitTest(NSPoint) -> Any?](../ObjectiveC/nsobject-swift.class/accessibilityhittest%28_%29.md)
- [var accessibilityNavigationStyle: UIAccessibilityNavigationStyle](../ObjectiveC/nsobject-swift.class/accessibilitynavigationstyle.md)
- [var accessibilityPath: UIBezierPath?](../ObjectiveC/nsobject-swift.class/accessibilitypath.md)
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](./uiaccessibility/zoomfocuschanged%28zoomtype,toframe,in%29.md)
  Notifies the system when the app’s focus changes to a new location.
- [UIAccessibility.ZoomType](./uiaccessibility/zoomtype.md)
  The types of system Zoom that can be in effect.
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)*