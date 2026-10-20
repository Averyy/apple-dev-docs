# textFinderMatchingTypeKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A number object containing the match type to use.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let textFinderMatchingTypeKey: NSPasteboard.PasteboardType.TextFinderOptionKey
```

```c
extern NSPasteboardTypeTextFinderOptionKey const NSTextFinderMatchingTypeKey;
```

#### Discussion

The value of this key must be an [`NSNumber`](../../../../Foundation/nsnumber.md) containing an [`NSTextFinder.MatchingType`](../../../nstextfinder/matchingtype.md) value that indicates the type of search matching to perform.

## See Also

### Option Keys
- [static let textFinderCaseInsensitiveKey: NSPasteboard.PasteboardType.TextFinderOptionKey](./textfindercaseinsensitivekey.md)
  A Boolean value indicating whether the search is case insensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/textfinderoptionkey/textfindermatchingtypekey)*