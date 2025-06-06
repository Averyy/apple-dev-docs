# recentSearches

**Framework**: AppKit  
**Kind**: property

The list of recent search strings for the control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var recentSearches: [String] { get set }
```

#### Discussion

An array of `NSString` objects, each of which contains a search string either displayed in the search menu or from a recent autosave archive. If there have been no recent searches and no prior searches saved under an autosave name, this array may be empty.

## See Also

- [var maximumRecents: Int](nssearchfield/maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [var recentsAutosaveName: NSSearchField.RecentsAutosaveName?](nssearchfield/recentsautosavename-swift.property.md)
  The name under which the search field automatically archives the list of recent search strings.
- [NSSearchField.RecentsAutosaveName](nssearchfield/recentsautosavename-swift.typealias.md)
  The string that stores the name under which a search field automatically archives a list of recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/recentsearches)*