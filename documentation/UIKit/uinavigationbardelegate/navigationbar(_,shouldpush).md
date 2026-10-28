# navigationBar(_:shouldPush:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the navigation bar should push an item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, shouldPush item: UINavigationItem) -> Bool
```

```objc
- (BOOL) navigationBar:(UINavigationBar *) navigationBar shouldPushItem:(UINavigationItem *) item;
```

## Return Value

[`true`](../../Swift/true.md) if the item should be pushed; otherwise, [`false`](../../Swift/false.md).

## Discussion

Sent to the delegate before pushing an item onto the navigation bar.

## Parameters

- `navigationBar`: The navigation bar that the item is being pushed onto.
- `item`: The navigation item that is being pushed.

## See Also

### Pushing items
- [func navigationBar(UINavigationBar, didPush: UINavigationItem)](./navigationbar%28_,didpush%29.md)
  Tells the delegate that an item was pushed onto the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpush:))*