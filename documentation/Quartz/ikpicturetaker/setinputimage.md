# setInputImage(_:)

**Framework**: Quartz  
**Kind**: method

Set the image input for the picture taker.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setInputImage(_ image: NSImage!)
```

#### Discussion

The input image is never modified by the picture taker.

## Parameters

- `image`: An   object.

## See Also

- [func inputImage() -> NSImage!](ikpicturetaker/inputimage.md)
  Returns the  input  image associated with the picture taker.
- [func outputImage() -> NSImage!](ikpicturetaker/outputimage.md)
  Returns the edited image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/setinputimage(_:))*