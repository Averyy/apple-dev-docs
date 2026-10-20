# ok(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action method that the panel calls when the user clicks the OK button.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func ok(_ sender: Any?)
```

```objc
- (void) ok:(id) sender;
```

#### Discussion

In macOS 10.15 and later, you cannot call this method programmatically to trigger the OK action. Prior to macOS 10.15, AppKit prevented only sandboxed apps from calling this method.

## Parameters

- `sender`: The [`NSSavePanel`](../nssavepanel.md) object that contains the OK button.

## See Also

### Handling Actions
- [func cancel(Any?)](./cancel%28_%29.md)
  The action method that the panel calls when the user clicks the Cancel button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/ok(_:))*