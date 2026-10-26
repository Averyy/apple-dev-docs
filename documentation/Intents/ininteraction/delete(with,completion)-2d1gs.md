# delete(with:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Deletes the specified interactions that were donated by the calling app.

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
class func delete(with identifiers: [String], completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func delete(with identifiers: [String]) async throws
```

```objc
+ (void) deleteInteractionsWithIdentifiers:(NSArray<NSString *> *) identifiers completion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Deleting Donated Shortcuts](../../SiriKit/deleting-donated-shortcuts.md)
- [Improving Siri Media Interactions and App Selection](../../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Discussion

Call this method to delete a specific set of donated Siri interactions. Typically, you delete interactions when they are no longer relevant. If you provide a block in the `completion` parameter, the system executes your block asynchronously with the results.

## Parameters

- `identifiers`: An array of strings containing the identifiers of the interactions that you want to delete. Each string corresponds to the value stored in the [`identifier`](./identifier.md) property of the interaction object.
- `completion`: A block to execute with the results. Provide a block if you want to know whether the deletion action was successful. The block has no return value and takes the following parameter.

  - **error**: An error object indicating a problem occurred. On success, this parameter is `nil`. If there was an error, this parameter contains an error object describing what happened.

## See Also

### Deleting Interactions from the System
- [class func deleteAll(completion: (((any Error)?) -> Void)?)](./deleteall%28completion%29.md)
  Deletes all interactions that you donated previously.
- [class func delete(with: String, completion: (((any Error)?) -> Void)?)](./delete%28with,completion%29-tcq9.md)
  Deletes the interactions with the specified group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/delete(with:completion:)-2d1gs)*