# init(attributedName:point:in:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new accessibility location descriptor using an attributed string and a specified point in a view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(attributedName: NSAttributedString, point: CGPoint, in view: UIView)
```

```objc
- (instancetype) initWithAttributedName:(NSAttributedString *) attributedName point:(CGPoint) point inView:(UIView *) view;
```

## See Also

### Initializing the descriptor
- [convenience init(name: String, point: CGPoint, in: UIView)](./init%28name,point,in%29.md)
  Initializes a new accessibility location descriptor with a specified point in a view.
- [convenience init(name: String, view: UIView)](./init%28name,view%29.md)
  Initializes a new accessibility location descriptor with a specified view’s activation point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/init(attributedname:point:in:))*