# image(forProposedSize:scaleFactor:imageOffset:imageSize:)

**Framework**: Core Text  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func image(forProposedSize proposedSize: CGSize, scaleFactor: CGFloat, imageOffset outImageOffset: UnsafeMutablePointer<CGPoint>, imageSize outImageSize: UnsafeMutablePointer<CGSize>) -> CGImage?
```

```objc
- (CGImageRef) imageForProposedSize:(CGSize) proposedSize scaleFactor:(CGFloat) scaleFactor imageOffset:(CGPoint *) outImageOffset imageSize:(CGSize *) outImageSize;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctadaptiveimageproviding/image(forproposedsize:scalefactor:imageoffset:imagesize:))*