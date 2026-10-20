# init(image:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a text attachment object to contain the specified image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(image: UIImage)
```

```objc
+ (NSTextAttachment *) textAttachmentWithImage:(UIImage *) image;
```

#### Return Value

A new text attachment object initialized with the image.

#### Discussion

Attachments created with this method automatically adapt to the surrounding font and color attributes in attributed strings.

For example, the following code creates a text attachment from the [`UIImage`](../uiimage.md) class using an SF symbol in a blue headline style and embeds it at the end of the [`NSMutableAttributedString`](../../Foundation/nsmutableattributedstring.md) class:

```swift
let content = NSMutableAttributedString(string: "Open ")
guard let lockImage = UIImage(systemName: "lock") else {
    return
}
let attributes: [NSAttributedString.Key: Any] = [
    .foregroundColor: UIColor.blue,
    .font: UIFont.preferredFont(forTextStyle: .headline)
]
let lockSymbol = NSMutableAttributedString(
    attachment: NSTextAttachment(image: lockImage)
)
lockSymbol.addAttributes(attributes, 
                         range: NSRange(location: 0, length: 1))
content.insert(lockSymbol, at: 5)

```

## Parameters

- `image`: The image for the attachment.

## See Also

### Initializing a text attachment
- [convenience init(fileWrapper: FileWrapper?)](../../AppKit/nstextattachment/init%28filewrapper%29.md)
  Creates a text attachment object to contain the specified file wrapper.
- [init(data: Data?, ofType: String?)](./init%28data,oftype%29.md)
  Creates a text attachment object with the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachment/init(image:))*