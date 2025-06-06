# init(frame:)

**Framework**: Quick Look UI  
**Kind**: init

Creates a preview view with the provided frame.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
init!(frame: NSRect)
```

#### Return Value

Returns a `QLPreviewView` object with the designated frame and the default style.

#### Discussion

Calling this method is equivalent to calling [`init(frame:style:)`](qlpreviewview/init(frame:style:).md) with the `style` parameter being [`QLPreviewViewStyle.normal`](qlpreviewviewstyle/normal.md).

## Parameters

- `frame`: The frame rectangle for the initialized   object.

## See Also

- [init!(frame: NSRect, style: QLPreviewViewStyle)](qlpreviewview/init(frame:style:).md)
  Creates a preview view with the provided frame and style.
- [enum QLPreviewViewStyle](qlpreviewviewstyle.md)
  Styles for a Preview View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/init(frame:))*