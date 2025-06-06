# onAppear(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform before this view appears.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onAppear(perform action: (() -> Void)? = nil) -> some View
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

#### Return Value

A view that triggers `action` before it appears.

#### Discussion

The exact moment that SwiftUI calls this method depends on the specific view type that you apply it to, but the `action` closure completes before the first rendered frame appears.

## Parameters

- `action`: The action to perform. If   is  , the   call has no effect.

## See Also

- [func onDisappear(perform: (() -> Void)?) -> some View](view/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func task(priority: TaskPriority, () async -> Void) -> some View](view/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](view/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onappear(perform:))*