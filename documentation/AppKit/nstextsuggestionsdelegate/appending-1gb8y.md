# appending(_:)

**Framework**: Appkit  
**Kind**: method

Returns a new text suggestions delegate of the same suggestion item type with the items and behaviors of the receiving delegate and `other` concatenated. When the returned delegate is connected to a text field, all suggestion items provided from the first suggestions delegate appear before all those from the second suggestions delegate, visually separated by a separator.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
func appending(_ other: some NSTextSuggestionsDelegate<Self.SuggestionItemType>) -> some NSTextSuggestionsDelegate<Self.SuggestionItemType>
```

#### Discussion

> **Note**: The returned aggregate text suggestions delegate strongly retains the given text suggestions delegate (`other`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextsuggestionsdelegate/appending(_:)-1gb8y)*