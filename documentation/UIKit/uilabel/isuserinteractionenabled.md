# isUserInteractionEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the system ignores and removes user events for this label from the event queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isUserInteractionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isUserInteractionEnabled) BOOL userInteractionEnabled;
```

## Discussion

[`UILabel`](../uilabel.md) inherits this property from the [`UIView`](../uiview.md) parent class. This class changes the default value of this property to [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var isUserInteractionEnabled: Bool](../uiview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
### Accessing additional attributes
- [clipsToBounds](../uilabel-clipstobounds.md)
  A Boolean value that determines whether subviews are confined to the bounds of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/isuserinteractionenabled)*