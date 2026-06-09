# maximumImageSize(forAspectRatio:)

**Framework**: CarPlay  
**Kind**: method

Returns the recommended maximum image size for a @c CPThumbnailImage with the given aspect ratio.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class func maximumImageSize(forAspectRatio aspectRatio: CGFloat) -> CGSize
```

#### Return Value

The recommended @c CGSize at which to size the image.

#### Discussion

Use this method to determine the correct size for images before providing them to

oversized images being held in the thumbnail pipeline.

## Parameters

- `aspectRatio`: The width-to-height ratio of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage/maximumimagesize(foraspectratio:))*