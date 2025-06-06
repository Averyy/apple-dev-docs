# replaceFormatDescription(_:with:)

**Framework**: AVFoundation  
**Kind**: method

Replaces the track’s format description with a new format description.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func replaceFormatDescription(_ formatDescription: CMFormatDescription, with newFormatDescription: CMFormatDescription)
```

#### Discussion

Use this method to change a track’s format descriptions, such as adding format description extensions to a format description or changing the audio channel layout of an audio track. Format description can have extensions of type [`kCMFormatDescriptionExtension_VerbatimSampleDescription`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_VerbatimSampleDescription) and [`kCMFormatDescriptionExtension_VerbatimISOSampleEntry`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_VerbatimISOSampleEntry). If you modify a copy of a format description, delete those extensions from the copy or your changes might be ignored.

## Parameters

- `formatDescription`: The   object to be replaced.
- `newFormatDescription`: The   object to replacing the specified format description.

## See Also

- [var formatDescriptions: [Any]](avmutablemovietrack/formatdescriptions.md)
  The format descriptions of the media samples that a track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/replaceformatdescription(_:with:))*