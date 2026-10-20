# lastResumeDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date when the activity was last resumed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var lastResumeDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * lastResumeDate;
```

#### Discussion

- If the activity was first started, this will be the same as the start date.
- If the activity was paused and resumed, this will be the date when the activity was resumed.

## See Also

### Getting the activity properties
- [var duration: TimeInterval](./duration.md)
  The total time elapsed while in active state.
- [var startDate: Date?](./startdate.md)
  The date when the activity was initially started.
- [var endDate: Date?](./enddate.md)
  The date when the activity was officially ended.
- [var creationDate: Date](./creationdate.md)
  The date when the activity was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/lastresumedate)*