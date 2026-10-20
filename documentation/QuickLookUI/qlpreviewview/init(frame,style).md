# init(frame:style:)

**Framework**: Quick Look UI  
**Kind**: init  
**Role**: Initializer

Creates a preview view with the provided frame and style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init!(frame: NSRect, style: QLPreviewViewStyle)
```

```objc
- (id) initWithFrame:(NSRect) frame style:(QLPreviewViewStyle) style;
```

#### Return Value

Returns a `QLPreviewView` object with the designated frame and style.

#### Discussion

This is the designated initializer for the `QLPreviewView` class.

## Parameters

- `frame`: The frame rectangle for the initialized `QLPreviewView` object.
- `style`: The desired style for the `QLPreviewView` object. For a list of possible styles, see [`QLPreviewViewStyle`](../qlpreviewviewstyle.md).

## See Also

### Creating a Preview View
- [init!(frame: NSRect)](./init%28frame%29.md)
  Creates a preview view with the provided frame.
- [enum QLPreviewViewStyle](../qlpreviewviewstyle.md)
  Styles for a Preview View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/init(frame:style:))*