# tagNames

**Framework**: AppKit  
**Kind**: property

The tag names that you want to include on a saved file.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var tagNames: [String]? { get set }
```

#### Discussion

When the value of [`showsTagField`](nssavepanel/showstagfield.md) is [`true`](https://developer.apple.com/documentation/swift/true), use this property to provide an array of strings that represent the initial tag names to display in the panel. If you set the property to `nil` or an empty array, the panel displays no initial tag names.

> **Note**:  The Tags field is appropriate only in a Save panel.

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
- [var accessoryView: NSView?](nssavepanel/accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](nssavepanel/showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/tagnames)*