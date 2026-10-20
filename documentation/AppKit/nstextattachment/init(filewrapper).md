# init(fileWrapper:)

**Framework**: AppKit  
**Kind**: init

Creates a text attachment object to contain the specified file wrapper.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init(fileWrapper: FileWrapper?)
```

#### Return Value

A new text attachment object initialized with the file wrapper.

#### Discussion

This method is the designated initializer for the [`NSTextAttachment`](nstextattachment.md) class in macOS.

If `aWrapper` contains an image file that the receiver can interpret as an [`NSImage`](nsimage.md) object, this method sets the attachment cell’s image to that image rather than to the icon of `aWrapper`.

## Parameters

- `fileWrapper`: The file wrapper for the attachment.

## See Also

- [init(data: Data?, ofType: String?)](nstextattachment/init(data:oftype:).md)
  Creates a text attachment object with the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/init(filewrapper:))*