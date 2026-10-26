# streamFormatWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new stream format with a format description and frame durations.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) streamFormatWithFormatDescription:(CMFormatDescriptionRef) formatDescription maxFrameDuration:(CMTime) maxFrameDuration minFrameDuration:(CMTime) minFrameDuration validFrameDurations:(NSArray<NSDictionary *> *) validFrameDurations;
```

## Parameters

- `formatDescription`: The format of the samples that a stream delivers.
- `maxFrameDuration`: The maximum frame duration the stream supports.
- `minFrameDuration`: The minimum frame duration the stream supports.
- `validFrameDurations`: A discrete set of supported frame durations.

## See Also

### Creating a Stream Format
- [- initWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:](./initwithformatdescription_maxframeduration_minframeduration_validframedurations_.md)
  Creates a stream format with a format description and frame durations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat/streamformatwithformatdescription:maxframeduration:minframeduration:validframedurations:)*