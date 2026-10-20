# endDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date when the activity was officially ended.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var endDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * endDate;
```

## See Also

### Getting the activity properties
- [var duration: TimeInterval](./duration.md)
  The total time elapsed while in active state.
- [var startDate: Date?](./startdate.md)
  The date when the activity was initially started.
- [var creationDate: Date](./creationdate.md)
  The date when the activity was created.
- [var lastResumeDate: Date?](./lastresumedate.md)
  The date when the activity was last resumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/enddate)*