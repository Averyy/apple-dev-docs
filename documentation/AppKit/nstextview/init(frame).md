# init(frame:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a text view.

**Availability**:
- macOS

## Declaration

```swift
init(frame frameRect: NSRect)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect;
```

#### Return Value

An initialized text view.

#### Discussion

This method creates the entire collection of objects associated with a text view—its text container, layout manager, and text storage—and invokes [`init(frame:textContainer:)`](./init%28frame,textcontainer%29.md).

This method creates the text web in such a manner that the text view is the principal owner of the objects in the web.

## Parameters

- `frameRect`: The frame rectangle of the text view.

## See Also

### Creating a text view
- [init(frame: NSRect, textContainer: NSTextContainer?)](./init%28frame,textcontainer%29.md)
  Initializes a text view.
- [convenience init(usingTextLayoutManager: Bool)](./init%28usingtextlayoutmanager%29.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a text view with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/init(frame:))*