# suggestedAge

**Framework**: ClassKit  
**Kind**: property

The range of ages, measured in years, for which you deem a context’s content suitable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var suggestedAge: NSRange { get set }
```

#### Discussion

Use this property to optionally suggest an age range for a context’s content. This guides teachers as they look for content for their students, although teachers are free to ignore your suggestion. If you provide a range, use integer ages measured in years as bounds. For example, you could consider a game as suitable for students from ages 4 to 6:

```swift
gameContext.suggestedAge = NSRange(4...6) // For ages 4 to 6.
```

To indicate no lower bound, provide a value of `0`. To indicate no upper bound, provide the largest possible value. Use both at the same time to indicate a context’s suitability for all ages:

```swift
youthContext.suggestedAge = NSRange(0...10) // Up to and including age 10.
adultContext.suggestedAge = NSRange(18...Int.max - 1) // Ages 18 and over.
allAgesContext.suggestedAge = NSRange(0...Int.max - 1) // For everyone.
```

New contexts that you create have the “all ages” setting by default.

> **Note**:  Because [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) defines its upper bound as one more than the last value contained in the range, use `Int.max - 1` to indicate the unbounded case and prevent the upper bound from overflowing.

## See Also

- [var suggestedCompletionTime: NSRange](clscontext/suggestedcompletiontime.md)
  A suggested time range to complete a task, measured in minutes.
- [var isAssignable: Bool](clscontext/isassignable.md)
  A Boolean that indicates whether teachers can assign the context as a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/suggestedage)*