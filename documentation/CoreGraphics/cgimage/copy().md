# copy()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates a copy of a bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy() -> CGImage?
```

```c
extern CGImageRefCGImageCreateCopy(CGImageRef image);
```

#### Return Value

An copy of the image.

## See Also

### Copying an image
- [func copy(colorSpace: CGColorSpace) -> CGImage?](./copy%28colorspace%29.md)
  Creates a copy of a bitmap image, replacing its colorspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/copy())*