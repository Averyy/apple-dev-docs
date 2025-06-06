# maximumRecents

**Framework**: AppKit  
**Kind**: property

The maximum number of search strings that can appear in the search menu.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var maximumRecents: Int { get set }
```

#### Discussion

The value of this property must be between 0 and 254. Specifying a negative value for the property sets it to the default value, which is 10. Specifying a value greater than 254 sets the property to 254.

When the maximum number of search strings is exceeded, the oldest search string on the menu is dropped.

## See Also

- [var recentSearches: [String]](nssearchfield/recentsearches.md)
  The list of recent search strings for the control.
- [var recentsAutosaveName: NSSearchField.RecentsAutosaveName?](nssearchfield/recentsautosavename-swift.property.md)
  The name under which the search field automatically archives the list of recent search strings.
- [NSSearchField.RecentsAutosaveName](nssearchfield/recentsautosavename-swift.typealias.md)
  The string that stores the name under which a search field automatically archives a list of recent search strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/maximumrecents)*