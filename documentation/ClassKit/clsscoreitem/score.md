# score

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The score earned by a user in completing the task.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var score: Double { get set }
```

```objc
@property (nonatomic, assign) double score;
```

## Discussion

Judge the value given against the activity item’s [`maxScore`](./maxscore.md). For example, if a quiz has eight questions, the maximum score might be 8, and the score might be an integer in the range `[0, 8]`.

## See Also

### Managing the Score
- [var maxScore: Double](./maxscore.md)
  The maximum possible score that the user can earn on a given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsscoreitem/score)*