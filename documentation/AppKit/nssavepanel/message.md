# message

**Framework**: AppKit  
**Kind**: property

The message text displayed in the panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var message: String! { get set }
```

#### Discussion

This prompt appears on all [`NSSavePanel`](nssavepanel.md) objects (or all [`NSOpenPanel`](nsopenpanel.md) objects if this property is on an [`NSOpenPanel`](nsopenpanel.md) instance) in your application. The default message text is an empty string.

## See Also

- [var title: String!](nssavepanel/title.md)
  The title of the panel.
- [var prompt: String!](nssavepanel/prompt.md)
  The text to display in the default button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/message)*