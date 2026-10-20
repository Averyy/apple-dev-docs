# animationDidStart(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the animation has started.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func animationDidStart(_ anim: CAAnimation)
```

```objc
- (void) animationDidStart:(CAAnimation *) anim;
```

## Parameters

- `anim`: The [`CAAnimation`](../caanimation.md) object that has started.

## See Also

### Customizing Start and Stop Times
- [func animationDidStop(CAAnimation, finished: Bool)](./animationdidstop%28_,finished%29.md)
  Tells the delegate the animation has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/animationdidstart(_:))*