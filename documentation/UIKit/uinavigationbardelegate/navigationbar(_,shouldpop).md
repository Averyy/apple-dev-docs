# navigationBar(_:shouldPop:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the navigation bar should pop an item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, shouldPop item: UINavigationItem) -> Bool
```

```objc
- (BOOL) navigationBar:(UINavigationBar *) navigationBar shouldPopItem:(UINavigationItem *) item;
```

#### Return Value

[`true`](../../Swift/true.md) if the item should be popped; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Sent to the delegate before popping an item from the navigation bar.

## Parameters

- `navigationBar`: The navigation bar that the item is being popped from.
- `item`: The navigation item that is being popped.

## See Also

### Popping items
- [func navigationBar(UINavigationBar, didPop: UINavigationItem)](./navigationbar%28_,didpop%29.md)
  Tells the delegate that an item was popped from the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpop:))*