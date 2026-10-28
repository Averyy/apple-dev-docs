# timescale

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The identifier’s timescale is the number of uniquely identifiable timestamps in a second.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var timescale: Int
```

## Discussion

For example an audio file sampled at 44,100 Hz should have a timescale value of 44,100 (or an integer multiple of that) so that every sample has a unique timestamp.

## See Also

### Getting the properties
- [var durationInSeconds: TimeInterval](./durationinseconds.md)
  The segment duration in seconds.
- [var range: Range<Int>](./range.md)
  The segment’s timestamp range.
- [var rangeInSeconds: Range<TimeInterval>](./rangeinseconds.md)
  The time range in seconds.
- [var source: String](./source.md)
  The segment source. For files use the full path or URL of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalsegmentidentifier/timescale)*