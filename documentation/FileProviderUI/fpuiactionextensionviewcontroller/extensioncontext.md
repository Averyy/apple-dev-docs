# extensionContext

**Framework**: File Provider UI  
**Kind**: property  
**Role**: Instance Property

The extension context provided by the host app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var extensionContext: FPUIActionExtensionContext { get }
```

```objc
@property (nonatomic, strong, readonly) FPUIActionExtensionContext * extensionContext;
```

## See Also

### Working with Actions
- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](./prepare%28foraction,itemidentifiers%29.md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](./prepare%28forerror%29.md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [class FPUIActionExtensionContext](../fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller/extensioncontext)*