# audiovisualTypes()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an array of the file types the asset supports.

**Availability**:
- iOS 5.0+ - Deprecated in 27.0
- iPadOS 5.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use audiovisualContentTypes instead

## Declaration

```swift
class func audiovisualTypes() -> [AVFileType]
```

```objc
+ (NSArray<NSString *> *) audiovisualTypes;
```

#### Return Value

An array of supported file types.

## See Also

### Determining supported media types
- [class func audiovisualMIMETypes() -> [String]](./audiovisualmimetypes%28%29.md)
  Returns an array of the MIME types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](./isplayableextendedmimetype%28_%29.md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
- [class var audiovisualContentTypes: [UTType]](./audiovisualcontenttypes.md)
  Provides the content types the AVURLAsset class understands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/audiovisualtypes())*