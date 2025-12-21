# main()

**Framework**: ExtensionFoundation  
**Kind**: method

The main entry point for an app extension that doesn’t present any UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency static func main() throws
```

#### Discussion

Don’t call this method directly. When the host launches your app extension in a new process, the system calls this method to create your custom [`AppExtension`](appextension.md) type and prepare your extension for requests from the host app.

## See Also

- [static func main() throws](appextension/main-w0u9.md)
  The main entry point for an app extension that doesn’t present any UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension/main()-5zfjx)*