# markupToolbarViewController(_:insertNewContents:)

**Framework**: PaperKit  
**Kind**: method

Add new content on top of the paper.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func markupToolbarViewController(_ markupToolbarViewController: MarkupToolbarViewController, insertNewContents toInsert: PaperMarkup)
```

#### Discussion

This is used for inserting any custom content, and non-shape elements like signatures or loupes.

## Parameters

- `markupToolbarViewController`: The source of the action.
- `toInsert`: The markup whose contents is added on top of this paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/markuptoolbarviewcontroller(_:insertnewcontents:))*