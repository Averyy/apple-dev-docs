# SignpostRecord

**Framework**: MetricKit  
**Kind**: struct

A record of a signpost event associated with a diagnostic report.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct SignpostRecord
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

This describes a single signpost event that was active around the time of a diagnostic event. Each record carries a subsystem, category, and name that identify the signpost, along with an [`interval`](signpostrecord/interval.md) covering the signpost’s duration. For instantaneous signposts, the start and end of the interval are equal, giving a duration of zero.

Access signpost records through [`signpostData`](diagnosticreport/environment-swift.struct/signpostdata.md) on the diagnostic report’s environment.

## Topics

### Signpost details
- [let subsystem: String](signpostrecord/subsystem.md)
  Signpost subsystem
- [let category: String](signpostrecord/category.md)
  Signpost category
- [let name: String](signpostrecord/name.md)
  Signpost name
### Timing
- [let interval: DateInterval](signpostrecord/interval.md)
  Time interval for the signpost For instant signposts, start and end are the same (duration == 0)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CallStackTree](callstacktree.md)
  A tree structure representing a collection of call stacks captured during a diagnostic event.
- [struct CallStackThread](callstackthread.md)
  A single stack thread within a call stack tree.
- [struct CallStackFrame](callstackframe.md)
  A single frame within a call stack thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signpostrecord)*