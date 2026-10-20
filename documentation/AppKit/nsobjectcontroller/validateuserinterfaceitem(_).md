# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver can handle the action method for a user interface item.

**Availability**:
- macOS

## Declaration

```swift
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

```objc
- (BOOL) validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>) item;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver can handle the action method; [`false`](../../Swift/false.md) if it cannot.

## Parameters

- `item`: The user interface item to validate. You can send `item` the [`action`](../nsvalidateduserinterfaceitem/action.md) and [`tag`](../nsvalidateduserinterfaceitem/tag.md) messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/validateuserinterfaceitem(_:))*