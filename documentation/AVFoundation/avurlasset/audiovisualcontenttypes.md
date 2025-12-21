# audiovisualContentTypes

**Framework**: AVFoundation  
**Kind**: property

Provides the content types the AVURLAsset class understands.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class var audiovisualContentTypes: [UTType] { get }
```

#### Return Value

An NSArray of UTTypes identifying the content types the AVURLAsset class understands.

## See Also

- [class func audiovisualTypes() -> [AVFileType]](avurlasset/audiovisualtypes.md)
  Returns an array of the file types the asset supports.
- [class func audiovisualMIMETypes() -> [String]](avurlasset/audiovisualmimetypes.md)
  Returns an array of the MIME types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](avurlasset/isplayableextendedmimetype(_:).md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualcontenttypes)*