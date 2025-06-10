# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Marks this view as searchable with text, tokens, and suggestions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the   search field.
- `suggestedTokens`: A collection of tokens to display as suggestions.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: Text resource for the localized prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-6hhqu)*