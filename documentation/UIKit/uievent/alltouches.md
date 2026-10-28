# allTouches

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

All touches associated with the event.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allTouches: Set<UITouch>? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSSet<UITouch *> * allTouches;
```

## Return Value

A set of [`UITouch`](../uitouch.md) objects representing all touches associated with the event.

## Discussion

If the touches of the event originate in different views and windows, the [`UITouch`](../uitouch.md) objects obtained from this method will be associated with different responder objects.

## See Also

### Getting the touches for an event
- [func touches(for: UIView) -> Set<UITouch>?](./touches%28for%29-9neb4.md)
  Returns the touch objects from the event that belong to the specified given view.
- [func touches(for: UIWindow) -> Set<UITouch>?](./touches%28for%29-767rm.md)
  Returns the touch objects from the event that belong to the specified window.
- [func coalescedTouches(for: UITouch) -> [UITouch]?](./coalescedtouches%28for%29.md)
  Returns all of the touches associated with the specified main touch.
- [func predictedTouches(for: UITouch) -> [UITouch]?](./predictedtouches%28for%29.md)
  Returns an array of touches that are predicted to occur for the specified touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/alltouches)*