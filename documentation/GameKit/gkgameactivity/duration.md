# duration

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The total time elapsed while in active state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval duration;
```

## See Also

### Getting the activity properties
- [var startDate: Date?](./startdate.md)
  The date when the activity was initially started.
- [var endDate: Date?](./enddate.md)
  The date when the activity was officially ended.
- [var creationDate: Date](./creationdate.md)
  The date when the activity was created.
- [var lastResumeDate: Date?](./lastresumedate.md)
  The date when the activity was last resumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/duration)*