# outputSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The settings to use for encoding media data you append to the output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputSettings: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * outputSettings;
```

#### Discussion

A value of `nil` indicates that the input passes the samples through to the output without reencoding them.

## See Also

### Inspecting an input
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the samples that the input accepts.
- [var sourceFormatHint: CMFormatDescription?](./sourceformathint.md)
  A hint about the format of the sample buffers to append to the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/outputsettings)*