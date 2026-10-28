# showsTagField

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel displays the Tags field.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var showsTagField: Bool { get set }
```

```objc
@property BOOL showsTagField;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel displays the Tags field; if [`false`](../../Swift/false.md), the panel doesn’t display the Tags field. The default value is [`true`](../../Swift/true.md). (Note that the Tags field is appropriate only in a Save panel.)

If you set this property to [`true`](../../Swift/true.md), you are responsible for setting tag names on the resulting file after saving is complete. If you don’t set this property, macOS will automatically show the tag field and attempt to apply the tags to the file. To set tags on files, use the [`tagNamesKey`](../../Foundation/urlresourcekey/tagnameskey.md).

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
- [var nameFieldStringValue: String](./namefieldstringvalue.md)
  The user-editable filename currently shown in the name field.
- [var directoryURL: URL?](./directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](./accessoryview.md)
  The custom accessory view for the current app.
- [var tagNames: [String]?](./tagnames.md)
  The tag names that you want to include on a saved file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/showstagfield)*