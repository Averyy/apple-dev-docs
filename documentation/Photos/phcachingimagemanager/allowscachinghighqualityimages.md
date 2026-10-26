# allowsCachingHighQualityImages

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the image manager prepares high-quality images.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.15+ - Deprecated in 26.0
- tvOS 10.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: This property is unused and will be removed in a future release

## Declaration

```swift
var allowsCachingHighQualityImages: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsCachingHighQualityImages;
```

#### Discussion

If `true` (the default), the image manager prepares images at high quality. This option produces better images, at a high performance cost.

For faster performance when preparing large numbers of images—such as while the user is scrolling quickly through a collection of thumbnails—set this property to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcachingimagemanager/allowscachinghighqualityimages)*