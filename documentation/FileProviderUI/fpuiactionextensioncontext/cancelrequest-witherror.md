# cancelRequest(withError:)

**Framework**: File Provider UI  
**Kind**: method

Cancels the action and returns the provided error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func cancelRequest(withError error: any Error)
```

## Mentions

- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)

#### Discussion

Call this method if the action fails. Set the error’s domain to [`FPUIErrorDomain`](fpuierrordomain.md). Set the error code to a [`FPUIExtensionErrorCode`](fpuiextensionerrorcode.md) value.

## See Also

- [func completeRequest()](fpuiactionextensioncontext/completerequest.md)
  Marks the action as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensioncontext/cancelrequest(witherror:))*