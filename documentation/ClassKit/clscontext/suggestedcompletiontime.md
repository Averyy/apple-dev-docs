# suggestedCompletionTime

**Framework**: ClassKit  
**Kind**: property

A suggested time range to complete a task, measured in minutes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var suggestedCompletionTime: NSRange { get set }
```

#### Discussion

Use this property to optionally indicate the time you expect students to need to complete the task associated with a context. The lower bound on the range indicates that you expect the task to take a least that many minutes. The upper bound indicates that you expect the task to take no more than that many minutes. For example, you can indicate that a quiz should take anywhere from 10 to 15 minutes to complete:

```swift
quizContext.suggestedCompletionTime = NSRange(10...15) // A short quiz.
```

To indicate no minimum time, provide a value of `0`. To indicate no maximum time, provide the largest possible value.

```swift
shortQuiz.suggestedAge = NSRange(0...10) // Up to 10 minutes.
chapterTest.suggestedAge = NSRange(20...Int.max - 1) // At least 20 minutes.
takeHomeExam.suggestedAge = NSRange(0...Int.max - 1) // No suggestion provided.
```

By default, new contexts use the extreme values to avoid indicating a suggested time range.

> **Note**:  Because [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) defines its upper bound as one more than the last value contained in the range, use `Int.max - 1` to indicate the unbounded case and prevent the upper bound from overflowing.

## See Also

- [var suggestedAge: NSRange](clscontext/suggestedage.md)
  The range of ages, measured in years, for which you deem a context’s content suitable.
- [var isAssignable: Bool](clscontext/isassignable.md)
  A Boolean that indicates whether teachers can assign the context as a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/suggestedcompletiontime)*