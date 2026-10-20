# setInputImage(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Set the image input for the picture taker.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setInputImage(_ image: NSImage!)
```

```objc
- (void) setInputImage:(NSImage *) image;
```

#### Discussion

The input image is never modified by the picture taker.

## Parameters

- `image`: An `NSImage` object.

## See Also

### Getting and Setting Images
- [func inputImage() -> NSImage!](./inputimage%28%29.md)
  Returns the  input  image associated with the picture taker.
- [func outputImage() -> NSImage!](./outputimage%28%29.md)
  Returns the edited image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/setinputimage(_:))*