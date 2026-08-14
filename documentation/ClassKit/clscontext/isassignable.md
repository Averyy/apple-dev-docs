# isAssignable

**Framework**: ClassKit  
**Kind**: property

A Boolean that indicates whether teachers can assign the context as a task.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isAssignable: Bool { get set }
```

#### Discussion

Set this Boolean to [`false`](https://developer.apple.com/documentation/swift/false) for a context that doesn’t represent an assignable task, like when you use a context solely as a container for other contexts. For example, if you add all of your app’s quiz contexts as the children of a single quiz collection context, you can mark the collection as “not assignable”:

```swift
collectionContext.isAssignable = false
```

This prevents the Schoolwork app from offering the collection as an assignment, while still presenting the collection as part of the context hierarchy. You don’t need to configure the individual quizzes as assignable, because the framework creates new contexts as assignable by default.

## See Also

- [var suggestedAge: NSRange](clscontext/suggestedage.md)
  The range of ages, measured in years, for which you deem a context’s content suitable.
- [var suggestedCompletionTime: NSRange](clscontext/suggestedcompletiontime.md)
  A suggested time range to complete a task, measured in minutes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/isassignable)*