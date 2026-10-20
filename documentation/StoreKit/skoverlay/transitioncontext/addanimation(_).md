# addAnimation(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Adds a closure you can use to animate view properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func addAnimation(_ block: @escaping () -> Void)
```

```objc
- (void) addAnimationBlock:(void (^)()) block;
```

## Parameters

- `block`: A closure that sets animatable view properties and runs on the main thread.

## See Also

### Adding an Animation
- [var startFrame: CGRect](./startframe.md)
  The size and location of the overlay before the transition.
- [var endFrame: CGRect](./endframe.md)
  The size and location of the overlay at the end of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext/addanimation(_:))*