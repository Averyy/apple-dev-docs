# playbackProgress

**Framework**: TV Services  
**Kind**: property

The percentage of the content that the user has already played, specified as a value between 0.0 and 1.0.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var playbackProgress: Double { get set }
```

#### Discussion

Use this property to specify how much of the content the user has already played. The value you specify must be in the range 0.0 to 1.0. If you specify numbers outside of that range, the system clamps them to the minimum or maximum values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectioneditem/playbackprogress)*