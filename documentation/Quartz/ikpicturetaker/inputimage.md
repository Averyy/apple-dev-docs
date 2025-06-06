# inputImage()

**Framework**: Quartz  
**Kind**: method

Returns the  input  image associated with the picture taker.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func inputImage() -> NSImage!
```

#### Return Value

The input image.

#### Discussion

The input image is never modified by the picture taker.

## See Also

- [func setInputImage(NSImage!)](ikpicturetaker/setinputimage(_:).md)
  Set the image input for the picture taker.
- [func outputImage() -> NSImage!](ikpicturetaker/outputimage.md)
  Returns the edited image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/inputimage())*