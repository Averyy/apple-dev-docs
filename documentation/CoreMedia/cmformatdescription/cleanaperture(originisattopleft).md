# cleanAperture(originIsAtTopLeft:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns the clean aperture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func cleanAperture(originIsAtTopLeft: Bool) -> CGRect
```

## Parameters

- `originIsAtTopLeft`: If `true`, the origin begins at the top-left corner of the rectangle instead of the bottom-left.

## See Also

### Working with Video Descriptions
- [func matchesImageBuffer(CVImageBuffer) -> Bool](./matchesimagebuffer%28_%29.md)
  Returns a Boolean value that indicates whether the format description matches an image buffer.
- [func presentationDimensions(usePixelAspectRatio: Bool, useCleanAperture: Bool) -> CGSize](./presentationdimensions%28usepixelaspectratio,usecleanaperture%29.md)
  Returns the dimensions to take the pixel aspect ratio or clean aperture into account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/cleanaperture(originisattopleft:))*