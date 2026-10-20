# FPUIActionExtensionContext

**Framework**: File Provider UI  
**Kind**: class  
**Role**: Class

An extension context provided to File Provider UI extensions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class FPUIActionExtensionContext
```

```objc
@interface FPUIActionExtensionContext : NSExtensionContext
```

## Mentions

- [Adding Actions to the Context Menu](./adding-actions-to-the-context-menu.md)

## Topics

### Completing the Action
- [func completeRequest()](./fpuiactionextensioncontext/completerequest%28%29.md)
  Marks the action as complete.
- [func cancelRequest(withError: any Error)](./fpuiactionextensioncontext/cancelrequest%28witherror%29.md)
  Cancels the action and returns the provided error.
### Identifying the Domain
- [var domainIdentifier: NSFileProviderDomainIdentifier?](./fpuiactionextensioncontext/domainidentifier.md)
  The identifier for the domain managed by the current file provider.
- [struct NSFileProviderDomainIdentifier](../FileProvider/nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Actions
- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](./fpuiactionextensionviewcontroller/prepare%28foraction,itemidentifiers%29.md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](./fpuiactionextensionviewcontroller/prepare%28forerror%29.md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [var extensionContext: FPUIActionExtensionContext](./fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensioncontext)*