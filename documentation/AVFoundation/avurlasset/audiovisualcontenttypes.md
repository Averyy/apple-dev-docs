# audiovisualContentTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSArray<UTType *> * audiovisualContentTypes;
```

#### Return Value

An NSArray of UTTypes identifying the content types the AVURLAsset class understands.

## See Also

### Determining supported media types
- [class func audiovisualTypes() -> [AVFileType]](./audiovisualtypes%28%29.md)
  Returns an array of the file types the asset supports.
- [class func audiovisualMIMETypes() -> [String]](./audiovisualmimetypes%28%29.md)
  Returns an array of the MIME types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](./isplayableextendedmimetype%28_%29.md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualcontenttypes)*