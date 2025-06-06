# isFindNavigatorVisible

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates when the find panel displays onscreen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isFindNavigatorVisible: Bool { get }
```

#### Discussion

The value of this property is `YES` when the find panel displays; otherwise, `NO`.

## See Also

- [var searchText: String?](uifindinteraction/searchtext.md)
  The search query with which to prepopulate the find panel’s search text field.
- [var replacementText: String?](uifindinteraction/replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.
- [var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)?](uifindinteraction/optionsmenuprovider.md)
  A closure that populates the search options for a find interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/isfindnavigatorvisible)*