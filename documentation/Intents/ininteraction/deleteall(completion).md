# deleteAll(completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Deletes all interactions that you donated previously.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func deleteAll(completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func deleteAll() async throws
```

```objc
+ (void) deleteAllInteractionsWithCompletion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Deleting Donated Shortcuts](../../SiriKit/deleting-donated-shortcuts.md)
- [Improving Siri Media Interactions and App Selection](../../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Discussion

Call this method to delete all of your app’s previously donated SiriKit interactions. If you provide a block in the `completion` parameter, the system executes your block asynchronously with the results.

> ❗ **Important**:  Typically, you only want to delete interactions that are no longer relevant. Use [`delete(with:completion:)`](./delete%28with,completion%29-2d1gs.md) to delete only interactions associated with a particular identifier.

## Parameters

- `completion`: A block to execute with the results. Provide a block if you want to know whether the deletion action succeeded. The block has no return value and takes the following parameter.

  - **error**: An error object indicating a problem occurred. On success, this parameter is `nil`. If there was an error, this parameter contains an error object describing what happened.

## See Also

### Deleting Interactions from the System
- [class func delete(with: [String], completion: (((any Error)?) -> Void)?)](./delete%28with,completion%29-2d1gs.md)
  Deletes the specified interactions that were donated by the calling app.
- [class func delete(with: String, completion: (((any Error)?) -> Void)?)](./delete%28with,completion%29-tcq9.md)
  Deletes the interactions with the specified group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/deleteall(completion:))*