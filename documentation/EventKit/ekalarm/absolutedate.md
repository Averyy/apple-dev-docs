# absoluteDate

**Framework**: EventKit  
**Kind**: property

The absolute date for the alarm.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var absoluteDate: Date? { get set }
```

#### Discussion

If you set this property for a relative offset alarm, it loses the relative offset and becomes an absolute alarm.

## See Also

- [var relativeOffset: TimeInterval](ekalarm/relativeoffset.md)
  The offset from the start of an event, at which the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/absolutedate)*