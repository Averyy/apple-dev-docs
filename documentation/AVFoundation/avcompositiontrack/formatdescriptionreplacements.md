# formatDescriptionReplacements

**Framework**: AVFoundation  
**Kind**: property

The replacement format descriptions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var formatDescriptionReplacements: [AVCompositionTrackFormatDescriptionReplacement] { get }
```

#### Discussion

The property’s values specify an original and a replacement format description, as set in a previous call to [`replaceFormatDescription(_:with:)`](avmutablecompositiontrack/replaceformatdescription(_:with:).md).

## See Also

- [var formatDescriptions: [Any]](avcompositiontrack/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [class AVCompositionTrackFormatDescriptionReplacement](avcompositiontrackformatdescriptionreplacement.md)
  An object that represents a format description and its replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/formatdescriptionreplacements)*