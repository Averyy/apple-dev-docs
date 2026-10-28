# prompt

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the default button.

**Availability**:
- macOS

## Declaration

```swift
var prompt: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * prompt;
```

## Discussion

The prompt appears on all [`NSSavePanel`](../nssavepanel.md) objects (or all [`NSOpenPanel`](../nsopenpanel.md) objects if this property is on an [`NSOpenPanel`](../nsopenpanel.md) instance) in your application. By default, the text in the default button is “Open” for an Open panel and “Save” for a Save panel.

Use short words or phrases, such as “Open,” “Save,” “Set,” or “Choose,” on the button. The button is not resized to accommodate long prompts.

## See Also

### Configuring the Panel’s Appearance
- [var title: String!](./title.md)
  The title of the panel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/prompt)*