# matchesImageBuffer(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the format description matches an image buffer.

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
func matchesImageBuffer(_ imageBuffer: CVImageBuffer) -> Bool
```

## Parameters

- `imageBuffer`: The image buffer to validate against.

## See Also

### Working with Video Descriptions
- [func cleanAperture(originIsAtTopLeft: Bool) -> CGRect](./cleanaperture%28originisattopleft%29.md)
  Returns the clean aperture.
- [func presentationDimensions(usePixelAspectRatio: Bool, useCleanAperture: Bool) -> CGSize](./presentationdimensions%28usepixelaspectratio,usecleanaperture%29.md)
  Returns the dimensions to take the pixel aspect ratio or clean aperture into account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/matchesimagebuffer(_:))*