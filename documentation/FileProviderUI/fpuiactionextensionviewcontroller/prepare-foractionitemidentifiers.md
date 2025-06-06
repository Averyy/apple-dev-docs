# prepare(forAction:itemIdentifiers:)

**Framework**: File Provider UI  
**Kind**: method

Performs any necessary setup or configuration for the specified action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepare(forAction actionIdentifier: String, itemIdentifiers: [NSFileProviderItemIdentifier])
```

## Mentions

- [Adding Actions to the Context Menu](adding-actions-to-the-context-menu.md)

#### Discussion

Use this method to prepare a user interface for handling the action. At a minimum, you should display feedback about the action.

For more information, see [`Adding Actions to the Context Menu`](adding-actions-to-the-context-menu.md).

## Parameters

- `actionIdentifier`: The identifier for the action performed by the user.
- `itemIdentifiers`: The identifiers of the items affected by the action.

## See Also

- [func prepare(forError: any Error)](fpuiactionextensionviewcontroller/prepare(forerror:).md)
  Performs any necessary setup or configuration when an authentication error occurs.
- [var extensionContext: FPUIActionExtensionContext](fpuiactionextensionviewcontroller/extensioncontext.md)
  The extension context provided by the host app.
- [class FPUIActionExtensionContext](fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:))*