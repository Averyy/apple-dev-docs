# initWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Creates a stream format with a format description and frame durations.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
- (instancetype) initWithFormatDescription:(CMFormatDescriptionRef) formatDescription maxFrameDuration:(CMTime) maxFrameDuration minFrameDuration:(CMTime) minFrameDuration validFrameDurations:(NSArray<NSDictionary *> *) validFrameDurations;
```

## Parameters

- `formatDescription`: The format of the samples that a stream delivers.
- `maxFrameDuration`: The maximum frame duration the stream supports.
- `minFrameDuration`: The minimum frame duration the stream supports.
- `validFrameDurations`: A discrete set of supported frame durations.

## See Also

### Creating a Stream Format
- [+ streamFormatWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:](./streamformatwithformatdescription_maxframeduration_minframeduration_validframedurations_.md)
  Returns a new stream format with a format description and frame durations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat/initwithformatdescription:maxframeduration:minframeduration:validframedurations:)*