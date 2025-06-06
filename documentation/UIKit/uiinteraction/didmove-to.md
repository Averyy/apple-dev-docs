# didMove(to:)

**Framework**: UIKit  
**Kind**: method  
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
@MainActor
func didMove(to view: UIView?)
```

## Parameters

- `view`: The view that owns and contains the interaction in its interaction array. If the view is  , the interaction’s owner removed the interaction from its interactions array.

## See Also

- [func willMove(to: UIView?)](uiinteraction/willmove(to:).md)
  Tells the interaction that a view will add or remove it from the view’s interactions array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinteraction/didmove(to:))*