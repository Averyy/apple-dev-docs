# init(frame:)

**Framework**: Quick Look UI  
**Kind**: init  
**Role**: Initializer

Creates a preview view with the provided frame.

**Availability**:
- macOS 10.6+

## Declaration

```swift
init!(frame: NSRect)
```

```objc
- (id) initWithFrame:(NSRect) frame;
```

#### Return Value

Returns a `QLPreviewView` object with the designated frame and the default style.

#### Discussion

Calling this method is equivalent to calling [`init(frame:style:)`](./init%28frame,style%29.md) with the `style` parameter being [`QLPreviewViewStyle.normal`](../qlpreviewviewstyle/normal.md).

## Parameters

- `frame`: The frame rectangle for the initialized `QLPreviewView` object.

## See Also

### Creating a Preview View
- [init!(frame: NSRect, style: QLPreviewViewStyle)](./init%28frame,style%29.md)
  Creates a preview view with the provided frame and style.
- [enum QLPreviewViewStyle](../qlpreviewviewstyle.md)
  Styles for a Preview View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/init(frame:))*