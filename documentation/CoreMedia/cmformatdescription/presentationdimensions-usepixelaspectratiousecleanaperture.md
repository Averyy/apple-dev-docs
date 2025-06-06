# presentationDimensions(usePixelAspectRatio:useCleanAperture:)

**Framework**: Core Media  
**Kind**: method

Returns the dimensions to take the pixel aspect ratio or clean aperture into account.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func presentationDimensions(usePixelAspectRatio: Bool = true, useCleanAperture: Bool = true) -> CGSize
```

## Parameters

- `usePixelAspectRatio`: If  , the function computes the dimensions maintaining the pixel aspect ratio.
- `useCleanAperture`: If  , the function computes the dimensions using the clean aperture.

## See Also

- [func cleanAperture(originIsAtTopLeft: Bool) -> CGRect](cmformatdescription/cleanaperture(originisattopleft:).md)
  Returns the clean aperture.
- [func matchesImageBuffer(CVImageBuffer) -> Bool](cmformatdescription/matchesimagebuffer(_:).md)
  Returns a Boolean value that indicates whether the format description matches an image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/presentationdimensions(usepixelaspectratio:usecleanaperture:))*