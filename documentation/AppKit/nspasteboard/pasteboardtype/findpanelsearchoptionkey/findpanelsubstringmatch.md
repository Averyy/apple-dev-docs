# findPanelSubstringMatch

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A number object containing the match type to use in the find panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let findPanelSubstringMatch: NSPasteboard.PasteboardType.FindPanelSearchOptionKey
```

```c
extern NSPasteboardTypeFindPanelSearchOptionKey NSFindPanelSubstringMatch;
```

## Discussion

The value of this key is an [`NSNumber`](../../../../Foundation/nsnumber.md) object containing one of the values defined in [`NSFindPanelSubstringMatchType`](../../../nsfindpanelsubstringmatchtype.md).

## See Also

### Constants
- [static let findPanelSearchOptions: NSPasteboard.PasteboardType](../findpanelsearchoptions.md)
  Type for the find panel metadata property list.
- [static let findPanelCaseInsensitiveSearch: NSPasteboard.PasteboardType.FindPanelSearchOptionKey](./findpanelcaseinsensitivesearch.md)
  A Boolean value indicating whether the search is case-insensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/findpanelsearchoptionkey/findpanelsubstringmatch)*