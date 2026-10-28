# recentsAutosaveName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name under which the search field automatically archives the list of recent search strings.

**Availability**:
- macOS

## Declaration

```swift
var recentsAutosaveName: NSSearchField.RecentsAutosaveName? { get set }
```

```objc
@property (copy, nullable) NSSearchFieldRecentsAutosaveName recentsAutosaveName;
```

## Discussion

Used as a key in the standard user defaults to save the recent searches. If you specify `nil` or an empty string for this property, no autosave name is set and searches aren’t autosaved.

## See Also

### Managing Recent Searches
- [var recentSearches: [String]](./recentsearches.md)
  The list of recent search strings for the control.
- [var maximumRecents: Int](./maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [NSSearchField.RecentsAutosaveName](./recentsautosavename-swift.typealias.md)
  The string that stores the name under which a search field automatically archives a list of recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/recentsautosavename-swift.property)*