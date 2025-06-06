# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the sender should be enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user interface item should be enabled, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `item`: The user interface item to validate. You can send   the   and   messages.

## See Also

- [User Interface Validation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/UIValidation.html#//apple_ref/doc/uid/10000040i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations/validateuserinterfaceitem(_:))*