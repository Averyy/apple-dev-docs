# score

**Framework**: ClassKit  
**Kind**: property

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

#### Discussion

Judge the value given against the activity item’s [`maxScore`](clsscoreitem/maxscore.md). For example, if a quiz has eight questions, the maximum score might be 8, and the score might be an integer in the range `[0, 8]`.

## See Also

- [var maxScore: Double](clsscoreitem/maxscore.md)
  The maximum possible score that the user can earn on a given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsscoreitem/score)*