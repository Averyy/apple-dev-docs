# isUserInteractionEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the system ignores and removes user events for this label from the event queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isUserInteractionEnabled: Bool { get set }
```

#### Discussion

[`UILabel`](uilabel.md) inherits this property from the [`UIView`](uiview.md) parent class. This class changes the default value of this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isUserInteractionEnabled: Bool](uiview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [clipsToBounds](uilabel-clipstobounds.md)
  A Boolean value that determines whether subviews are confined to the bounds of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/isuserinteractionenabled)*