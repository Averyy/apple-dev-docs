# init(imageContent:)

**Framework**: AppKit  
**Kind**: init

Create an adaptive image glyph from the previously saved data.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(imageContent: Data)
```

#### Return Value

A new adaptive image glyph with the identifier and details from the image data.

#### Discussion

Use this initializer to create an adaptive image glyph from data you previously saved.

## Parameters

- `imageContent`: The raw image data you obtained previously from an adaptive image glyph. Typically, you receive adaptive images from the text system, store their data with the rest of your content, and use the data to recreate the adaptive image later.

## See Also

- [init(coder: NSCoder)](nsadaptiveimageglyph/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsadaptiveimageglyph/init(imagecontent:))*