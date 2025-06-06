# CGImageSourceUpdateData(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Updates the data in an incremental image source.

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
func CGImageSourceUpdateData(_ isrc: CGImageSource, _ data: CFData, _ final: Bool)
```

#### Discussion

This method updates the state of the image source and its contained images. Call this method one or more times to update the contents of an incremental data source. Each time you call the method, you must specify all of the accumulated image data, not just the new data you received.

## Parameters

- `isrc`: The image source to modify.
- `data`: The updated data for the image source. Each time you call this function, specify all of the accumulated image data so far.
- `final`: A Boolean value that indicates whether the   parameter represents the complete data set. Specify   if the data is complete or   if it isn’t.

## See Also

- [func CGImageSourceUpdateDataProvider(CGImageSource, CGDataProvider, Bool)](cgimagesourceupdatedataprovider(_:_:_:).md)
  Updates an incremental image source with a new data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourceupdatedata(_:_:_:))*