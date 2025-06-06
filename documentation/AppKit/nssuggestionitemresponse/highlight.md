# NSSuggestionItemResponse.Highlight

**Framework**: AppKit  
**Kind**: enum

Describes the possible ways the highlighted item may be impacted by these results

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Highlight
```

## Topics

### Enumeration Cases
- [NSSuggestionItemResponse.Highlight.automatic](nssuggestionitemresponse/highlight/automatic.md)
  The highlighted item is managed automatically by the control This is useful in contexts where the results, while still relevant, aren’t an incredibly strong match, or suggestions are a secondary means of input, deferring to text the user has entered themselves.
- [NSSuggestionItemResponse.Highlight.firstSelectableItem](nssuggestionitemresponse/highlight/firstselectableitem.md)
  The first selectable item (if any) should be highlighted, indicating a strong match This is useful in contexts where suggestions are less for convenience and are instead expected to be the primary way for users to interact with the control.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemresponse/highlight)*