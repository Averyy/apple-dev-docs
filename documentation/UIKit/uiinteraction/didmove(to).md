# didMove(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the interaction that a view added or removed it from the view’s interactions array.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func didMove(to view: UIView?)
```

```objc
- (void) didMoveToView:(UIView *) view;
```

## Parameters

- `view`: The view that owns and contains the interaction in its interaction array. If the view is `nil`, the interaction’s owner removed the interaction from its interactions array.

## See Also

### Tracking the Movements
- [func willMove(to: UIView?)](./willmove%28to%29.md)
  Tells the interaction that a view will add or remove it from the view’s interactions array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinteraction/didmove(to:))*