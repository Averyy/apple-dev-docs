# CGImageSourceUpdateDataProvider(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Updates an incremental image source with a new data provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageSourceUpdateDataProvider(_ isrc: CGImageSource, _ provider: CGDataProvider, _ final: Bool)
```

## Parameters

- `isrc`: The image source to modify.
- `provider`: The new data provider. The new data provider must provide all the previous data supplied to the image source and any additional new data.
- `final`: A Boolean value that indicates whether the   parameter provides the complete data set. Specify   if the data is complete or   if it isn’t.

## See Also

- [func CGImageSourceUpdateData(CGImageSource, CFData, Bool)](cgimagesourceupdatedata(_:_:_:).md)
  Updates the data in an incremental image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourceupdatedataprovider(_:_:_:))*