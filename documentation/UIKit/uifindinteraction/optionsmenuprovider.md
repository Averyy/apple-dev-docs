# optionsMenuProvider

**Framework**: UIKit  
**Kind**: property

A closure that populates the search options for a find interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)? { get set }
```

#### Discussion

You use this closure to modify, augement or omit options from the default set available in [`UITextSearchOptions`](uitextsearchoptions.md).

## See Also

- [var isFindNavigatorVisible: Bool](uifindinteraction/isfindnavigatorvisible.md)
  A Boolean value that indicates when the find panel displays onscreen.
- [var searchText: String?](uifindinteraction/searchtext.md)
  The search query with which to prepopulate the find panel’s search text field.
- [var replacementText: String?](uifindinteraction/replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/optionsmenuprovider)*