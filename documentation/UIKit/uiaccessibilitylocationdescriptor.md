# UIAccessibilityLocationDescriptor

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An accessibility descriptor for a specific geometric point of interest within a view, for use by assistive apps.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityLocationDescriptor
```

```objc
@interface UIAccessibilityLocationDescriptor : NSObject
```

## Topics

### Initializing the descriptor
- [init(attributedName: NSAttributedString, point: CGPoint, in: UIView)](./uiaccessibilitylocationdescriptor/init%28attributedname,point,in%29.md)
  Initializes a new accessibility location descriptor using an attributed string and a specified point in a view.
- [convenience init(name: String, point: CGPoint, in: UIView)](./uiaccessibilitylocationdescriptor/init%28name,point,in%29.md)
  Initializes a new accessibility location descriptor with a specified point in a view.
- [convenience init(name: String, view: UIView)](./uiaccessibilitylocationdescriptor/init%28name,view%29.md)
  Initializes a new accessibility location descriptor with a specified view’s activation point.
### Getting the descriptor information
- [var name: String](./uiaccessibilitylocationdescriptor/name.md)
  Returns the plaintext string representation of the name for the accessibility location descriptor.
- [var attributedName: NSAttributedString](./uiaccessibilitylocationdescriptor/attributedname.md)
  Returns the attributed string representation of the name for the accessibility location descriptor.
- [var point: CGPoint](./uiaccessibilitylocationdescriptor/point.md)
  Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.
- [var view: UIView?](./uiaccessibilitylocationdescriptor/view.md)
  Returns the view associated with the accessibility location descriptor.
### Initializers
- [init(attributedName: NSAttributedString, point: CGPoint, inView: UIView)](./uiaccessibilitylocationdescriptor/init%28attributedname,point,inview%29.md)
- [convenience init(name: String, point: CGPoint, inView: UIView)](./uiaccessibilitylocationdescriptor/init%28name,point,inview%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor)*