# tagNames

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tag names that you want to include on a saved file.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var tagNames: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * tagNames;
```

## Discussion

When the value of [`showsTagField`](./showstagfield.md) is [`true`](../../Swift/true.md), use this property to provide an array of strings that represent the initial tag names to display in the panel. If you set the property to `nil` or an empty array, the panel displays no initial tag names.

> **Note**:  The Tags field is appropriate only in a Save panel.

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
- [var showsTagField: Bool](./showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/tagnames)*