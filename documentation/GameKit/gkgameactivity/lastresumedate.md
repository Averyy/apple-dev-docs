# lastResumeDate

**Framework**: GameKit  
**Kind**: property

The date when the activity was last resumed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var lastResumeDate: Date? { get }
```

#### Discussion

- If the activity was first started, this will be the same as the start date.
- If the activity was paused and resumed, this will be the date when the activity was resumed.

## See Also

- [var duration: TimeInterval](gkgameactivity/duration.md)
  Total time elapsed while in active state.
- [var startDate: Date?](gkgameactivity/startdate.md)
  The date when the activity was initially started.
- [var endDate: Date?](gkgameactivity/enddate.md)
  The date when the activity was officially ended.
- [var creationDate: Date](gkgameactivity/creationdate.md)
  The date when the activity was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/lastresumedate)*