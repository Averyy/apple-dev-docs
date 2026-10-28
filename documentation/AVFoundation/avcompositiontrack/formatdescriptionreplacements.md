# formatDescriptionReplacements

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSArray<AVCompositionTrackFormatDescriptionReplacement *> * formatDescriptionReplacements;
```

## Discussion

The property’s values specify an original and a replacement format description, as set in a previous call to [`replaceFormatDescription(_:with:)`](../avmutablecompositiontrack/replaceformatdescription%28_,with%29.md).

## See Also

### Managing format descriptions
- [var formatDescriptions: [Any]](./formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [class AVCompositionTrackFormatDescriptionReplacement](../avcompositiontrackformatdescriptionreplacement.md)
  An object that represents a format description and its replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/formatdescriptionreplacements)*