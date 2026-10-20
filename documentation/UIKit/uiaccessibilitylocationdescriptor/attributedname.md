# attributedName

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the attributed string representation of the name for the accessibility location descriptor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var attributedName: NSAttributedString { get }
```

```objc
@property (nonatomic, strong, readonly) NSAttributedString * attributedName;
```

## See Also

### Getting the descriptor information
- [var name: String](./name.md)
  Returns the plaintext string representation of the name for the accessibility location descriptor.
- [var point: CGPoint](./point.md)
  Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.
- [var view: UIView?](./view.md)
  Returns the view associated with the accessibility location descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/attributedname)*