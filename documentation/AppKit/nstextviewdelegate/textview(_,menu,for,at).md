# textView(_:menu:for:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows delegate to control the context menu returned by the text view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, menu: NSMenu, for event: NSEvent, at charIndex: Int) -> NSMenu?
```

```objc
- (NSMenu *) textView:(NSTextView *) view menu:(NSMenu *) menu forEvent:(NSEvent *) event atIndex:(NSUInteger) charIndex;
```

#### Return Value

A menu to use as the contextual menu. You can return `menu` unaltered, or you can return a customized menu.

#### Discussion

This method allows the delegate to control the context menu returned by [`menu(for:)`](../nsview/menu%28for%29.md).

## Parameters

- `view`: The text view sending the message.
- `menu`: The proposed contextual menu.
- `event`: The mouse-down event that initiated the contextual menu’s display.
- `charIndex`: The character position where the mouse button was clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:menu:for:at:))*