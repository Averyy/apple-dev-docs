# nameFieldStringValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The user-editable filename currently shown in the name field.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var nameFieldStringValue: String { get set }
```

```objc
@property (copy) NSString * nameFieldStringValue;
```

#### Discussion

The value of this property must not be `nil`. Note that the filename may not display an extension if the value of [`isExtensionHidden`](./isextensionhidden.md) is [`true`](../../Swift/true.md).

## See Also

### Configuring the Panel’s Appearance
- [var title: String!](./title.md)
  The title of the panel.
- [var prompt: String!](./prompt.md)
  The text to display in the default button.
- [var message: String!](./message.md)
  The message text displayed in the panel.
- [var nameFieldLabel: String!](./namefieldlabel.md)
  The label text displayed in front of the filename text field.
- [var directoryURL: URL?](./directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](./accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](./showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](./tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/namefieldstringvalue)*