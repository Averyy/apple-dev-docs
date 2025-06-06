# target

**Framework**: Core Media  
**Kind**: property

A time range on the target timeline.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var target: CMTimeRange
```

#### Discussion

If the target and source have different durations, the source segment should play at a rate of `source.duration / target.duration` to fit.

## See Also

- [var source: CMTimeRange](cmtimemapping/source.md)
  A time range on the source timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapping/target)*