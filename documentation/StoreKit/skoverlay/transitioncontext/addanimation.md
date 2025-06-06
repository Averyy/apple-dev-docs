# addAnimation(_:)

**Framework**: StoreKit  
**Kind**: method

Adds a closure you can use to animate view properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func addAnimation(_ block: @escaping () -> Void)
```

## Parameters

- `block`: A closure that sets animatable view properties and runs on the main thread.

## See Also

- [var startFrame: CGRect](skoverlay/transitioncontext/startframe.md)
  The size and location of the overlay before the transition.
- [var endFrame: CGRect](skoverlay/transitioncontext/endframe.md)
  The size and location of the overlay at the end of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext/addanimation(_:))*