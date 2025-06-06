# view

**Framework**: UIKit  
**Kind**: property

Returns the view associated with the accessibility location descriptor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var view: UIView? { get }
```

## See Also

- [var name: String](uiaccessibilitylocationdescriptor/name.md)
  Returns the plaintext string representation of the name for the accessibility location descriptor.
- [var attributedName: NSAttributedString](uiaccessibilitylocationdescriptor/attributedname.md)
  Returns the attributed string representation of the name for the accessibility location descriptor.
- [var point: CGPoint](uiaccessibilitylocationdescriptor/point.md)
  Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/view)*