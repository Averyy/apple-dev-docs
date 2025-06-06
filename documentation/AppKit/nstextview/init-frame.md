# init(frame:)

**Framework**: AppKit  
**Kind**: init

Initializes a text view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(frame frameRect: NSRect)
```

#### Return Value

An initialized text view.

#### Discussion

This method creates the entire collection of objects associated with a text view—its text container, layout manager, and text storage—and invokes [`init(frame:textContainer:)`](nstextview/init(frame:textcontainer:).md).

This method creates the text web in such a manner that the text view is the principal owner of the objects in the web.

## Parameters

- `frameRect`: The frame rectangle of the text view.

## See Also

- [init(frame: NSRect, textContainer: NSTextContainer?)](nstextview/init(frame:textcontainer:).md)
  Initializes a text view.
- [convenience init(usingTextLayoutManager: Bool)](nstextview/init(usingtextlayoutmanager:).md)
- [init?(coder: NSCoder)](nstextview/init(coder:).md)
  Initializes a text view with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/init(frame:))*