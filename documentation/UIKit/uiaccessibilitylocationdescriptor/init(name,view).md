# init(name:view:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new accessibility location descriptor with a specified view’s activation point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, view: UIView)
```

```objc
- (instancetype) initWithName:(NSString *) name view:(UIView *) view;
```

## See Also

### Initializing the descriptor
- [init(attributedName: NSAttributedString, point: CGPoint, in: UIView)](./init%28attributedname,point,in%29.md)
  Initializes a new accessibility location descriptor using an attributed string and a specified point in a view.
- [convenience init(name: String, point: CGPoint, in: UIView)](./init%28name,point,in%29.md)
  Initializes a new accessibility location descriptor with a specified point in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/init(name:view:))*