# init(formatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:)

**Framework**: Core Media I/O  
**Kind**: init

Creates a stream format with a format description and frame durations.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
convenience init(formatDescription: CMFormatDescription, maxFrameDuration: CMTime, minFrameDuration: CMTime, validFrameDurations: [CMTime]?)
```

## Parameters

- `formatDescription`: The format of the samples that a stream delivers.
- `maxFrameDuration`: The maximum frame duration the stream supports.
- `minFrameDuration`: The minimum frame duration the stream supports.
- `validFrameDurations`: A discrete set of supported frame durations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat/init(formatdescription:maxframeduration:minframeduration:validframedurations:))*