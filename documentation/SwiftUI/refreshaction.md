# RefreshAction

**Framework**: SwiftUI  
**Kind**: struct

An action that initiates a refresh operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct RefreshAction
```

#### Overview

When the [`refresh`](environmentvalues/refresh.md) environment value contains an instance of this structure, certain built-in views in the corresponding [`Environment`](environment.md) begin offering a refresh capability. They apply the instance’s handler to any refresh operation that the user initiates. By default, the environment value is `nil`, but you can use the [`refreshable(action:)`](view/refreshable(action:).md) modifier to create and store a new refresh action that uses the handler that you specify:

```swift
List(mailbox.conversations) { conversation in
    ConversationCell(conversation)
}
.refreshable {
    await mailbox.fetch()
}
```

On iOS and iPadOS, the [`List`](list.md) in the example above offers a pull to refresh gesture because it detects the refresh action. When the user drags the list down and releases, the list calls the action’s handler. Because SwiftUI declares the handler as asynchronous, it can safely make long-running asynchronous calls, like fetching network data.

##### Refreshing Custom Views

You can also offer refresh capability in your custom views. Read the [`refresh`](environmentvalues/refresh.md) environment value to get the `RefreshAction` instance for a given [`Environment`](environment.md). If you find a non-`nil` value, change your view’s appearance or behavior to offer the refresh to the user, and call the instance to conduct the refresh. You can call the refresh instance directly because it defines a [`callAsFunction()`](refreshaction/callasfunction().md) method that Swift calls when you call the instance:

```swift
struct RefreshableView: View {
    @Environment(\.refresh) private var refresh

    var body: some View {
        Button("Refresh") {
            Task {
                await refresh?()
            }
        }
        .disabled(refresh == nil)
    }
}
```

Be sure to call the handler asynchronously by preceding it with `await`. Because the call is asynchronous, you can use its lifetime to indicate progress to the user. For example, you might reveal an indeterminate [`ProgressView`](progressview.md) before calling the handler, and hide it when the handler completes.

If your code isn’t already in an asynchronous context, create a [`Task`](https://developer.apple.com/documentation/Swift/Task) for the method to run in. If you do this, consider adding a way for the user to cancel the task. For more information, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in .

## Topics

### Calling the action
- [func callAsFunction() async](refreshaction/callasfunction.md)
  Initiates a refresh action.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func refreshable(action: () async -> Void) -> some View](view/refreshable(action:).md)
  Marks this view as refreshable.
- [var refresh: RefreshAction?](environmentvalues/refresh.md)
  A refresh action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/refreshaction)*