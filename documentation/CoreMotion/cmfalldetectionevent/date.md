# date

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The event’s time and date.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
var date: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * date;
```

#### Discussion

Use the `date` to identify a fall event. The system guarantees fall events have different `date` values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/date)*