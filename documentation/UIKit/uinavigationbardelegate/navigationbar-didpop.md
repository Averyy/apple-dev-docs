# navigationBar(_:didPop:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that an item was popped from the navigation bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationBar(_ navigationBar: UINavigationBar, didPop item: UINavigationItem)
```

#### Discussion

If animating the pop operation, this method is invoked after the animation ends; otherwise, it is invoked immediately after the pop.

## Parameters

- `navigationBar`: The navigation bar that the item is being popped from.
- `item`: The navigation item that is being popped.

## See Also

- [func navigationBar(UINavigationBar, shouldPop: UINavigationItem) -> Bool](uinavigationbardelegate/navigationbar(_:shouldpop:).md)
  Returns a Boolean value indicating whether the navigation bar should pop an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:didpop:))*