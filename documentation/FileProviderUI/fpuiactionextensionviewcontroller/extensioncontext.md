# extensionContext

**Framework**: File Provider UI  
**Kind**: property

The extension context provided by the host app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var extensionContext: FPUIActionExtensionContext { get }
```

## See Also

- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](fpuiactionextensionviewcontroller/prepare(forerror:).md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [class FPUIActionExtensionContext](fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller/extensioncontext)*