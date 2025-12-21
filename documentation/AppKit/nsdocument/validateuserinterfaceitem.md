# validateUserInterfaceItem(_:)

**Framework**: AppKit  
**Kind**: method

Validates the specified user interface item that the receiver manages.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateUserInterfaceItem(_ item: any NSValidatedUserInterfaceItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the item is valid; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

These items currently include only Revert and Save. You can override this method to add more selectors validated by your document subclass.

## Parameters

- `item`: The user interface item to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/validateuserinterfaceitem(_:))*