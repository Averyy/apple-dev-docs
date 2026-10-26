# setRelevantShortcuts(_:completionHandler:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Sets the relevant shortcuts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setRelevantShortcuts(_ shortcuts: [INRelevantShortcut], completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func setRelevantShortcuts(_ shortcuts: [INRelevantShortcut]) async throws
```

```objc
- (void) setRelevantShortcuts:(NSArray<INRelevantShortcut *> *) shortcuts completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

#### Discussion

Call this method to give Siri the list of relevant shortcuts for your app. To replace the list, call the method again, passing in a new list of relevant shortcuts. If you want to remove all relevant shortcuts associated with your app, call the method passing in an empty array.

To ensure the system stores the relevant shortcuts, wait for the system to call the `completionHandler` block.

## Parameters

- `shortcuts`: A list of relevant shortcuts.
- `completionHandler`: The block invoked on a background thread after the system stores the relevant shortcuts. This block has no return value and takes the following parameter:

  - **`error`**: An [`NSError`](../../Foundation/nserror.md) object if a problem occurred storing the relevant shortcuts; otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcutstore/setrelevantshortcuts(_:completionhandler:))*