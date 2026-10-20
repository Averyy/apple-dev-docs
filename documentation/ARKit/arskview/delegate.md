# delegate

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An object you provide to mediate synchronization of the view’s AR scene information with SpriteKit content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
weak var delegate: (any ARSKViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) NSObject<ARSKViewDelegate> * delegate;
```

## See Also

### Responding to AR Updates
- [protocol ARSKViewDelegate](../arskviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SpriteKit content with an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/delegate)*