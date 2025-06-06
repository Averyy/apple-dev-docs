# isPlayableExtendedMIMEType(_:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the asset is playable with the specified codec and container type; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `extendedMIMEType`: An extended MIME type string such as   or  .

## See Also

- [class func audiovisualTypes() -> [AVFileType]](avurlasset/audiovisualtypes.md)
  Returns an array of the file types the asset supports.
- [class func audiovisualMIMETypes() -> [String]](avurlasset/audiovisualmimetypes.md)
  Returns an array of the MIME types the asset supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/isplayableextendedmimetype(_:))*