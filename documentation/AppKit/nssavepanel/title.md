# title

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title of the panel.

**Availability**:
- macOS

## Declaration

```swift
var title: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * title;
```

## Discussion

By default, “Save” is the title string. If you adapt the `NSSavePanel` object for other uses, its title should reflect the user action that brings it to the screen.

## See Also

### Configuring the Panel’s Appearance
- [var prompt: String!](./prompt.md)
  The text to display in the default button.
- [var message: String!](./message.md)
  The message text displayed in the panel.
- [var nameFieldLabel: String!](./namefieldlabel.md)
  The label text displayed in front of the filename text field.
- [var nameFieldStringValue: String](./namefieldstringvalue.md)
  The user-editable filename currently shown in the name field.
- [var directoryURL: URL?](./directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](./accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](./showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](./tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/title)*