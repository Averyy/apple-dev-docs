# navigationBar(_:shouldPush:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether the navigation bar should push an item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationBar(_ navigationBar: UINavigationBar, shouldPush item: UINavigationItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the item should be pushed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Sent to the delegate before pushing an item onto the navigation bar.

## Parameters

- `navigationBar`: The navigation bar that the item is being pushed onto.
- `item`: The navigation item that is being pushed.

## See Also

- [func navigationBar(UINavigationBar, didPush: UINavigationItem)](uinavigationbardelegate/navigationbar(_:didpush:).md)
  Tells the delegate that an item was pushed onto the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpush:))*