# showsTagField

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel displays the Tags field.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var showsTagField: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the panel displays the Tags field; if [`false`](https://developer.apple.com/documentation/Swift/false), the panel doesn’t display the Tags field. The default value is [`true`](https://developer.apple.com/documentation/Swift/true). (Note that the Tags field is appropriate only in a Save panel.)

If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true), you are responsible for setting tag names on the resulting file after saving is complete. If you don’t set this property, macOS will automatically show the tag field and attempt to apply the tags to the file. To set tags on files, use the [`tagNamesKey`](https://developer.apple.com/documentation/Foundation/URLResourceKey/tagNamesKey).

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
- [var tagNames: [String]?](nssavepanel/tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/showstagfield)*