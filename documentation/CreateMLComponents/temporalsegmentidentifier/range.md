# range

**Framework**: Create ML Components  
**Kind**: property

The segment’s timestamp range.

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
var range: Range<Int>
```

#### Discussion

To get a timestamp in seconds divide the value by the timescale.

## See Also

- [var durationInSeconds: TimeInterval](temporalsegmentidentifier/durationinseconds.md)
  The segment duration in seconds.
- [var rangeInSeconds: Range<TimeInterval>](temporalsegmentidentifier/rangeinseconds.md)
  The time range in seconds.
- [var source: String](temporalsegmentidentifier/source.md)
  The segment source. For files use the full path or URL of the file.
- [var timescale: Int](temporalsegmentidentifier/timescale.md)
  The identifier’s timescale is the number of uniquely identifiable timestamps in a second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalsegmentidentifier/range)*