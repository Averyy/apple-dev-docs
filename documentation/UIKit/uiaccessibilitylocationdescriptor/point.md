# point

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var point: CGPoint { get }
```

```objc
@property (nonatomic, readonly) CGPoint point;
```

## See Also

### Getting the descriptor information
- [var name: String](./name.md)
  Returns the plaintext string representation of the name for the accessibility location descriptor.
- [var attributedName: NSAttributedString](./attributedname.md)
  Returns the attributed string representation of the name for the accessibility location descriptor.
- [var view: UIView?](./view.md)
  Returns the view associated with the accessibility location descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/point)*