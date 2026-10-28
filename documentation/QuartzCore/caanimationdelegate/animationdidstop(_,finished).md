# animationDidStop(_:finished:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the animation has ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func animationDidStop(_ anim: CAAnimation, finished flag: Bool)
```

```objc
- (void) animationDidStop:(CAAnimation *) anim finished:(BOOL) flag;
```

## Discussion

The animation may have ended because it has completed its active duration or because it has been removed from the layer it is attached to. `flag` is true if the animation reached the end of its duration without being removed.

## Parameters

- `anim`: The [`CAAnimation`](../caanimation.md) object that has ended.
- `flag`: A flag indicating whether the animation has completed by reaching the end of its duration.

## See Also

### Customizing Start and Stop Times
- [func animationDidStart(CAAnimation)](./animationdidstart%28_%29.md)
  Tells the delegate the animation has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/animationdidstop(_:finished:))*