# title

**Framework**: AppKit  
**Kind**: property

The title of the panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var title: String! { get set }
```

#### Discussion

By default, “Save” is the title string. If you adapt the `NSSavePanel` object for other uses, its title should reflect the user action that brings it to the screen.

## See Also

- [var prompt: String!](nssavepanel/prompt.md)
  The text to display in the default button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/title)*