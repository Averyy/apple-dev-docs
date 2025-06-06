# searchable(text:placement:prompt:suggestions:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: S, @ViewBuilder suggestions: () -> V) -> some View where V : View, S : StringProtocol
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: Where the search field should attempt to be   placed based on the containing view hierarchy.
- `prompt`: A string representing the prompt of the search field   which provides users with guidance on what to search for.
- `suggestions`: A view builder that produces content that   populates a list of suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/searchable(text:placement:prompt:suggestions:)-4u1ru)*