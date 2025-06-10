# delegate

**Framework**: ExtensionKit  
**Kind**: property

The connection delegate.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+

## Declaration

```swift
@MainActor
weak var delegate: (any EXHostViewControllerDelegate)? { get set }
```

## See Also

- [func makeXPCConnection() throws -> NSXPCConnection](exhostviewcontroller/makexpcconnection.md)
  Attempts to connect to the extension over XPC.
- [protocol EXHostViewControllerDelegate](exhostviewcontrollerdelegate.md)
  The delegate for a hosted view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/delegate)*