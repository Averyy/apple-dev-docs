# SearchScopeActivation

**Framework**: SwiftUI  
**Kind**: struct

The ways that searchable modifiers can show or hide search scopes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
struct SearchScopeActivation
```

## Mentions

- [Scoping a search operation](scoping-a-search-operation.md)

## Topics

### Getting search scope activiation types
- [static var automatic: SearchScopeActivation](searchscopeactivation/automatic.md)
  The automatic activation of the scope bar.
- [static var onSearchPresentation: SearchScopeActivation](searchscopeactivation/onsearchpresentation.md)
  An activation where the system shows search scopes after presenting search and hides search scopes after search cancellation.
- [static var onTextEntry: SearchScopeActivation](searchscopeactivation/ontextentry.md)
  An activation where the system shows search scopes when typing begins in the search field and hides search scopes after search cancellation.

## See Also

- [Scoping a search operation](scoping-a-search-operation.md)
  Divide the search space into a few broad categories.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](view/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](view/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchscopeactivation)*