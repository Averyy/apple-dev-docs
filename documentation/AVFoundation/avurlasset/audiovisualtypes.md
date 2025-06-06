# audiovisualTypes()

**Framework**: AVFoundation  
**Kind**: method

Returns an array of the file types the asset supports.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func audiovisualTypes() -> [AVFileType]
```

#### Return Value

An array of supported file types.

## See Also

- [class func audiovisualMIMETypes() -> [String]](avurlasset/audiovisualmimetypes.md)
  Returns an array of the MIME types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](avurlasset/isplayableextendedmimetype(_:).md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualtypes())*