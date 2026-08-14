# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether to enable the specified item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified item responds to [`toggleSidebar(_:)`](nssplitviewcontroller/togglesidebar(_:).md), [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t.

## Parameters

- `item`: The user interface item to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/validateuserinterfaceitem(_:))*