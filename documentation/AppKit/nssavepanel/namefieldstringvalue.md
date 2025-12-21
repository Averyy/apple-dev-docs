# nameFieldStringValue

**Framework**: AppKit  
**Kind**: property

The user-editable filename currently shown in the name field.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var nameFieldStringValue: String { get set }
```

#### Discussion

The value of this property must not be `nil`. Note that the filename may not display an extension if the value of [`isExtensionHidden`](nssavepanel/isextensionhidden.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var title: String!](nssavepanel/title.md)
  The title of the panel.
- [var prompt: String!](nssavepanel/prompt.md)
  The text to display in the default button.
- [var message: String!](nssavepanel/message.md)
  The message text displayed in the panel.
- [var nameFieldLabel: String!](nssavepanel/namefieldlabel.md)
  The label text displayed in front of the filename text field.
- [var directoryURL: URL?](nssavepanel/directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](nssavepanel/accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](nssavepanel/showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](nssavepanel/tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/namefieldstringvalue)*