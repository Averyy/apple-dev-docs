# textFinderCaseInsensitiveKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value indicating whether the search is case insensitive.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let textFinderCaseInsensitiveKey: NSPasteboard.PasteboardType.TextFinderOptionKey
```

```c
extern NSPasteboardTypeTextFinderOptionKey const NSTextFinderCaseInsensitiveKey;
```

#### Discussion

The value of this key must be an [`NSValue`](../../../../Foundation/nsvalue.md) object containing a Boolean value. The value [`true`](../../../../Swift/true.md) indicates a case-insensitive search; [`false`](../../../../Swift/false.md) indicates a case-sensitive search.

## See Also

### Option Keys
- [static let textFinderMatchingTypeKey: NSPasteboard.PasteboardType.TextFinderOptionKey](./textfindermatchingtypekey.md)
  A number object containing the match type to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/textfinderoptionkey/textfindercaseinsensitivekey)*