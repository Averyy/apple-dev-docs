# recentsAutosaveName

**Framework**: AppKit  
**Kind**: property

The name under which the search field automatically archives the list of recent search strings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var recentsAutosaveName: NSSearchField.RecentsAutosaveName? { get set }
```

#### Discussion

Used as a key in the standard user defaults to save the recent searches. If you specify `nil` or an empty string for this property, no autosave name is set and searches aren’t autosaved.

## See Also

- [var recentSearches: [String]](nssearchfield/recentsearches.md)
  The list of recent search strings for the control.
- [var maximumRecents: Int](nssearchfield/maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [NSSearchField.RecentsAutosaveName](nssearchfield/recentsautosavename-swift.typealias.md)
  The string that stores the name under which a search field automatically archives a list of recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/recentsautosavename-swift.property)*