# recentsAutosaveName

**Framework**: AppKit  
**Kind**: property

The autosave name under which the search field automatically saves the list of recent search strings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var recentsAutosaveName: NSSearchField.RecentsAutosaveName? { get set }
```

#### Discussion

The autosave name is used as a key in the standard user defaults to save the recent searches. If you specify `nil` or an empty string for this parameter, no autosave name is set and searches are not automatically saved.

## See Also

- [var maximumRecents: Int](nssearchfieldcell/maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [var recentSearches: [String]!](nssearchfieldcell/recentsearches.md)
  An array of the recent search strings to display in the pop-up icon menu of the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/recentsautosavename)*