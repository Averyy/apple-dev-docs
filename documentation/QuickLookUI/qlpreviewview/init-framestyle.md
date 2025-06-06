# init(frame:style:)

**Framework**: Quick Look UI  
**Kind**: init

Creates a preview view with the provided frame and style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
init!(frame: NSRect, style: QLPreviewViewStyle)
```

#### Return Value

Returns a `QLPreviewView` object with the designated frame and style.

#### Discussion

This is the designated initializer for the `QLPreviewView` class.

## Parameters

- `frame`: The frame rectangle for the initialized   object.
- `style`: The desired style for the   object. For a list of possible styles, see  .

## See Also

- [init!(frame: NSRect)](qlpreviewview/init(frame:).md)
  Creates a preview view with the provided frame.
- [enum QLPreviewViewStyle](qlpreviewviewstyle.md)
  Styles for a Preview View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/init(frame:style:))*