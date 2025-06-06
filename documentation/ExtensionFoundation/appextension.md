# AppExtension

**Framework**: ExtensionFoundation  
**Kind**: protocol

Declares a type used by app extensions.

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
protocol AppExtension
```

## Topics

### Creating an App Extension
- [init()](appextension/init.md)
  Creates a new app extension.
### Implementing an App Extension
- [var configuration: Self.Configuration](appextension/configuration-swift.property.md)
  The configuration object for this app extension.
- [associatedtype Configuration : AppExtensionConfiguration](appextension/configuration-swift.associatedtype.md)
  A type that provides the app extension configuration information.
- [static func main() throws](appextension/main-5zfjx.md)
  The main entry point for a non-UI extension.
- [static func main() throws](appextension/main-w0u9.md)
  The main entry point for a UI extension.
### Default Implementations
- [AppExtension Implementations](appextension/appextension-implementations.md)

## See Also

- [struct AppExtensionIdentity](appextensionidentity.md)
  An object that uniquely identifies an app extension.
- [protocol AppExtensionConfiguration](appextensionconfiguration.md)
  An object that holds configuration options for an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension)*