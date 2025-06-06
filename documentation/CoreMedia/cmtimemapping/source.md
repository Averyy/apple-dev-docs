# source

**Framework**: Core Media  
**Kind**: property

A time range on the source timeline.

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
var source: CMTimeRange
```

#### Discussion

For an empty edit, `source.start` is an invalid `CMTime`, in which case the system ignores `source.duration`. Otherwise, `source.start` is the starting time within the source, and `source.duration` is the duration of the source timeline to map to the target time range.

## See Also

- [var target: CMTimeRange](cmtimemapping/target.md)
  A time range on the target timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapping/source)*