# markupToolbarViewController(_:insertNewContents:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add new content on top of the paper.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func markupToolbarViewController(_ markupToolbarViewController: MarkupToolbarViewController, insertNewContents toInsert: PaperMarkup)
```

#### Discussion

This is used for inserting any custom content, and non-shape elements like signatures or loupes.

## Parameters

- `markupToolbarViewController`: The source of the action.
- `toInsert`: The markup whose contents is added on top of this paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewcontents:))*