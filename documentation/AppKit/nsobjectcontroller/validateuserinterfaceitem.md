# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method

Returns whether the receiver can handle the action method for a user interface item.

**Availability**:
- macOS ?+

## Declaration

```swift
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver can handle the action method; [`false`](https://developer.apple.com/documentation/swift/false) if it cannot.

## Parameters

- `item`: The user interface item to validate. You can send   the   and   messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/validateuserinterfaceitem(_:))*