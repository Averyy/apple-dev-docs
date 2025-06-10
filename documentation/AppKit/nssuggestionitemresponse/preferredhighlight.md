# preferredHighlight

**Framework**: AppKit  
**Kind**: property

The preferred response that the control should take when this batch of results comes in (like whether or not to highlight the first selectable item). Defaults to `.automatic`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var preferredHighlight: NSSuggestionItemResponse<SuggestionItemType>.Highlight
```

#### Discussion

> **Note**: This value is just a hint to the control on how to actually respond and may not  affect the highlighted item. In the case that the user has begun to already make a selection by using the up/down arrow keys, or using the mouse, the actual highlighted item may not be affected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemresponse/preferredhighlight)*