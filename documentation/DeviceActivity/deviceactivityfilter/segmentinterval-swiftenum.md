# DeviceActivityFilter.SegmentInterval

**Framework**: DeviceActivity  
**Kind**: enum

A type indicating the interval at which the system subdivides device activity data within a specified date interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum SegmentInterval
```

## Topics

### Operators
- [static func == (DeviceActivityFilter.SegmentInterval, DeviceActivityFilter.SegmentInterval) -> Bool](deviceactivityfilter/segmentinterval-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [DeviceActivityFilter.SegmentInterval.daily(during:)](deviceactivityfilter/segmentinterval-swift.enum/daily(during:).md)
  Indicates that the system aggregates data into daily segments within the specified interval.
- [DeviceActivityFilter.SegmentInterval.hourly(during:)](deviceactivityfilter/segmentinterval-swift.enum/hourly(during:).md)
  Indicates that the system aggregates data into hourly segments within the specified interval.
- [DeviceActivityFilter.SegmentInterval.weekly(during:)](deviceactivityfilter/segmentinterval-swift.enum/weekly(during:).md)
  Indicates that the system aggregates data into weekly segments within the specified interval.
### Instance Properties
- [var hashValue: Int](deviceactivityfilter/segmentinterval-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivityfilter/segmentinterval-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](deviceactivityfilter/segmentinterval-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/segmentinterval-swift.enum)*