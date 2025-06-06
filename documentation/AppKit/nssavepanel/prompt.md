# prompt

**Framework**: AppKit  
**Kind**: property

The text to display in the default button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var prompt: String! { get set }
```

#### Discussion

The prompt appears on all [`NSSavePanel`](nssavepanel.md) objects (or all [`NSOpenPanel`](nsopenpanel.md) objects if this property is on an [`NSOpenPanel`](nsopenpanel.md) instance) in your application. By default, the text in the default button is “Open” for an Open panel and “Save” for a Save panel.

Use short words or phrases, such as “Open,” “Save,” “Set,” or “Choose,” on the button. The button is not resized to accommodate long prompts.

## See Also

- [var title: String!](nssavepanel/title.md)
  The title of the panel.
- [var message: String!](nssavepanel/message.md)
  The message text displayed in the panel.
- [var nameFieldLabel: String!](nssavepanel/namefieldlabel.md)
  The label text displayed in front of the filename text field.
- [var nameFieldStringValue: String](nssavepanel/namefieldstringvalue.md)
  The user-editable filename currently shown in the name field.
- [var directoryURL: URL?](nssavepanel/directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](nssavepanel/accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](nssavepanel/showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](nssavepanel/tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/prompt)*