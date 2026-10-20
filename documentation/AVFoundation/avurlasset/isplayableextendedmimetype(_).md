# isPlayableExtendedMIMEType(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.

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
class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool
```

```objc
+ (BOOL) isPlayableExtendedMIMEType:(NSString *) extendedMIMEType;
```

#### Return Value

[`true`](../../Swift/true.md) if the asset is playable with the specified codec and container type; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `extendedMIMEType`: An extended MIME type string such as `video/3gpp2; codecs=“mp4v.20.9, mp4a.E1”` or `audio/aac; codecs=“mp4a.E1”`.

## See Also

### Determining supported media types
- [class func audiovisualTypes() -> [AVFileType]](./audiovisualtypes%28%29.md)
  Returns an array of the file types the asset supports.
- [class func audiovisualMIMETypes() -> [String]](./audiovisualmimetypes%28%29.md)
  Returns an array of the MIME types the asset supports.
- [class var audiovisualContentTypes: [UTType]](./audiovisualcontenttypes.md)
  Provides the content types the AVURLAsset class understands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/isplayableextendedmimetype(_:))*