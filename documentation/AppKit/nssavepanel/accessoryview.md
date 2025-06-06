# accessoryView

**Framework**: AppKit  
**Kind**: property

The custom accessory view for the current app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var accessoryView: NSView? { get set }
```

#### Discussion

You can customize the panel by adding a custom view. The custom object you add appears just above the OK and Cancel buttons at the bottom of the panel. The `NSSavePanel` object automatically resizes itself to accommodate `accessoryView`. Use this property to change the accessory view as needed. If `accessoryView` is `nil`, the Save panel removes the current accessory view.

The panel relinquishes ownership of the accessory view after the panel is closed. If you want to reuse the accessory view, don’t rely on the panel to hold onto the accessory view until the next time you use it; instead, maintain your own strong reference to the view.

## See Also

- [var title: String!](nssavepanel/title.md)
  The title of the panel.
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
- [var showsTagField: Bool](nssavepanel/showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](nssavepanel/tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/accessoryview)*