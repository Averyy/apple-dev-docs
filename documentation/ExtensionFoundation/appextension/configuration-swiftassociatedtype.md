# Configuration

**Framework**: ExtensionFoundation  
**Kind**: associatedtype  
**Required**: Yes

A type that provides the app extension configuration information.

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
associatedtype Configuration : AppExtensionConfiguration
```

#### Discussion

When you create a custom app extension, Swift infers this type from your implementation of the required [`configuration`](appextension/configuration-swift.property.md) property.

## See Also

- [var configuration: Self.Configuration](appextension/configuration-swift.property.md)
  The configuration object for this app extension.
- [static func main() throws](appextension/main-5zfjx.md)
  The main entry point for a non-UI extension.
- [static func main() throws](appextension/main-w0u9.md)
  The main entry point for a UI extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension/configuration-swift.associatedtype)*