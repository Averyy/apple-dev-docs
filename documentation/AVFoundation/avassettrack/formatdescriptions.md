# formatDescriptions

**Framework**: AVFoundation  
**Kind**: property

The format descriptions of the media samples that a track references.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var formatDescriptions: [Any] { get }
```

## Mentions

- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)

#### Discussion

The array contains [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription) objects that indicate the format of media samples the track references.

Asset tracks typically present uniform media (for example, media that uses the same encoding settings) and contain a single format description. However, in some cases, an asset track may contain multiple format descriptions. For example, an H.264-encoded video track may have some segments that use the Main profile and others that use the High profile. Also, an individual [`AVCompositionTrack`](avcompositiontrack.md), which subclasses [`AVAssetTrack`](avassettrack.md), may contain audio or video segments using different codecs.

You can use [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription) to access low-level details about the media the track references. For example, you can retrieve the details of track’s media type and subtype as the code below shows:

```swift
extension AVAssetTrack {
    var mediaFormat: String {
        var format = ""
        let descriptions = self.formatDescriptions as! [CMFormatDescription]
        for (index, formatDesc) in descriptions.enumerated() {
            // Get a string representation of the media type.
            let type =
                CMFormatDescriptionGetMediaType(formatDesc).toString()
            // Get a string representation of the media subtype.
            let subType =
                CMFormatDescriptionGetMediaSubType(formatDesc).toString()
            // Format the string as type/subType, such as vide/avc1 or soun/aac.
            format += "\(type)/\(subType)"
            // Comma-separate if there's more than one format description.
            if index < descriptions.count - 1 {
                format += ","
            }
        }
        return format
    }
}
 
extension FourCharCode {
    // Create a string representation of a FourCC.
    func toString() -> String {
        let bytes: [CChar] = [
            CChar((self >> 24) & 0xff),
            CChar((self >> 16) & 0xff),
            CChar((self >> 8) & 0xff),
            CChar(self & 0xff),
            0
        ]
        let result = String(cString: bytes)
        let characterSet = CharacterSet.whitespaces
        return result.trimmingCharacters(in: characterSet)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/formatdescriptions)*