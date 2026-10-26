# PHImageRequestOptionsResizeMode.fast

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case fast
```

```c
PHImageRequestOptionsResizeModeFast
```

#### Discussion

With this option, Photos can use image subsampling to quickly provide an image at a size roughly matching the target size.

## See Also

### Constants
- [PHImageRequestOptionsResizeMode.none](./none.md)
  Photos does not resize the image asset.
- [PHImageRequestOptionsResizeMode.exact](./exact.md)
  Photos resizes the image to match the target size exactly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode/fast)*