# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether a given user interface item should be enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `item` should be enabled, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Subclasses can override this method to perform additional validations. Subclasses should call the underlying method on `super` in their implementation for items they don’t handle themselves.

## Parameters

- `item`: The user interface item to validate. You can send   the   and   messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/validateuserinterfaceitem(_:))*