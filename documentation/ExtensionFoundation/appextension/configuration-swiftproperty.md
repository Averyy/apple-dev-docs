# configuration

**Framework**: ExtensionFoundation  
**Kind**: property  
**Required**: Yes

The configuration object for this app extension.

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
@preconcurrency var configuration: Self.Configuration { get }
```

## See Also

- [associatedtype Configuration : AppExtensionConfiguration](appextension/configuration-swift.associatedtype.md)
  A type that provides the app extension configuration information.
- [static func main() throws](appextension/main-5zfjx.md)
  The main entry point for a non-UI extension.
- [static func main() throws](appextension/main-w0u9.md)
  The main entry point for a UI extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension/configuration-swift.property)*