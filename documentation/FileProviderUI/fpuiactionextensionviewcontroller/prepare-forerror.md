# prepare(forError:)

**Framework**: File Provider UI  
**Kind**: method

Performs any necessary setup or configuration when an authentication error occurs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepare(forError error: any Error)
```

#### Discussion

While your file provider is enumerating its content, the system calls this method whenever your file provider returns an [`NSFileProviderErrorDomain`](https://developer.apple.com/documentation/FileProvider/NSFileProviderErrorDomain) error with a [`NSFileProviderError.Code.notAuthenticated`](https://developer.apple.com/documentation/FileProvider/NSFileProviderError/Code/notAuthenticated) code. Use this method to present an interface to authenticate the user.

## Parameters

- `error`: An object representing the authentication error. Your File Provider extension can pass additional information in the error’s   property.

## See Also

- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md)
  Performs any necessary setup or configuration for the specified action.
- [var extensionContext: FPUIActionExtensionContext](fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.
- [class FPUIActionExtensionContext](fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller/prepare(forerror:))*