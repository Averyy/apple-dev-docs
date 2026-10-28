# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the sender should be enabled.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

```objc
- (BOOL) validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>) item;
```

## Return Value

[`true`](../../Swift/true.md) if the user interface item should be enabled, otherwise [`false`](../../Swift/false.md).

## Parameters

- `item`: The user interface item to validate. You can send `anItem` the [`action`](../nsvalidateduserinterfaceitem/action.md) and [`tag`](../nsvalidateduserinterfaceitem/tag.md) messages.

## See Also

### Related Documentation
- [User Interface Validation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/UIValidation.html#//apple_ref/doc/uid/10000040i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations/validateuserinterfaceitem(_:))*