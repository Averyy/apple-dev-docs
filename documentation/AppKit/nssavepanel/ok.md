# ok(_:)

**Framework**: AppKit  
**Kind**: method

The action method that the panel calls when the user clicks the OK button.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func ok(_ sender: Any?)
```

#### Discussion

In macOS 10.15 and later, you cannot call this method programmatically to trigger the OK action. Prior to macOS 10.15, AppKit prevented only sandboxed apps from calling this method.

## Parameters

- `sender`: The   object that contains the OK button.

## See Also

- [func cancel(Any?)](nssavepanel/cancel(_:).md)
  The action method that the panel calls when the user clicks the Cancel button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/ok(_:))*