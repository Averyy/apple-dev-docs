# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether to enable the specified item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

```objc
- (BOOL) validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>) item;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified item responds to [`toggleSidebar(_:)`](./togglesidebar%28_%29.md), [`false`](../../Swift/false.md) if it doesn’t.

## Parameters

- `item`: The user interface item to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/validateuserinterfaceitem(_:))*