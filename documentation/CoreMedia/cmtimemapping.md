# CMTimeMapping

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that maps a segment of a source time range to a target time range.

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
struct CMTimeMapping
```

```c
typedef struct { ... } CMTimeMapping;
```

## Topics

### Creating a Timebase
- [init(source: CMTimeRange, target: CMTimeRange)](./cmtimemapping/init%28source,target%29.md)
  Creates a time mapping with a source and target time range.
- [init()](./cmtimemapping/init%28%29.md)
  Creates an empty time mapping.
### Accessing Time Ranges
- [var source: CMTimeRange](./cmtimemapping/source.md)
  A time range on the source timeline.
- [var target: CMTimeRange](./cmtimemapping/target.md)
  A time range on the target timeline.
### Type Properties
- [static let invalid: CMTimeMapping](./cmtimemapping/invalid.md)
  An invalid time mapping.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapping)*