# FPUIActionExtensionContext

**Framework**: File Provider UI  
**Kind**: class

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

## Mentions

- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)

## Topics

### Completing the Action
- [func completeRequest()](fpuiactionextensioncontext/completerequest.md)
  Marks the action as complete.
- [func cancelRequest(withError: any Error)](fpuiactionextensioncontext/cancelrequest(witherror:).md)
  Cancels the action and returns the provided error.
### Identifying the Domain
- [var domainIdentifier: NSFileProviderDomainIdentifier?](fpuiactionextensioncontext/domainidentifier.md)
  The identifier for the domain managed by the current file provider.
- [struct NSFileProviderDomainIdentifier](../FileProvider/NSFileProviderDomainIdentifier.md)
  A unique identifier for a file provider’s domain.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md)
  Performs any necessary setup or configuration for the specified action.
- [func prepare(forError: any Error)](fpuiactionextensionviewcontroller/prepare(forerror:).md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [var extensionContext: FPUIActionExtensionContext](fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensioncontext)*