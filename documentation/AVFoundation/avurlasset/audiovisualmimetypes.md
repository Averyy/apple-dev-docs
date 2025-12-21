# audiovisualMIMETypes()

**Framework**: AVFoundation  
**Kind**: method

Returns an array of the MIME types the asset supports.

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
class func audiovisualMIMETypes() -> [String]
```

#### Return Value

An array of MIME type strings.

## See Also

- [class func audiovisualTypes() -> [AVFileType]](avurlasset/audiovisualtypes.md)
  Returns an array of the file types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](avurlasset/isplayableextendedmimetype(_:).md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
- [class var audiovisualContentTypes: [UTType]](avurlasset/audiovisualcontenttypes.md)
  Provides the content types the AVURLAsset class understands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualmimetypes())*