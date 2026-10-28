# delete(with:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Deletes the interactions with the specified group identifier.

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
class func delete(with groupIdentifier: String, completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func delete(with groupIdentifier: String) async throws
```

```objc
+ (void) deleteInteractionsWithGroupIdentifier:(NSString *) groupIdentifier completion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Deleting Donated Shortcuts](../../SiriKit/deleting-donated-shortcuts.md)

## Discussion

Call this method to delete a group of donated Siri interactions. Typically, you delete interactions when they are no longer relevant. For example, if you have associated an interaction identifier with a playlist, you can delete all the interactions about the list if the user deletes it.

If you provide a block in the `completion` parameter, the system executes your block asynchronously with the results.

## Parameters

- `groupIdentifier`: The group identifier string of the interactions that you want to delete. This string corresponds to the value stored in the [`groupIdentifier`](./groupidentifier.md) property of the interaction objects.
- `completion`: A block to execute with the results. Provide a block if you want to know whether the deletion action succeeded. The block has no return value and takes the following parameter.

  - **error**: An error object indicating a problem occurred. On success, this parameter is `nil`. If there was an error, this parameter contains an error object describing what happened.

## See Also

### Deleting Interactions from the System
- [class func deleteAll(completion: (((any Error)?) -> Void)?)](./deleteall%28completion%29.md)
  Deletes all interactions that you donated previously.
- [class func delete(with: [String], completion: (((any Error)?) -> Void)?)](./delete%28with,completion%29-2d1gs.md)
  Deletes the specified interactions that were donated by the calling app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/delete(with:completion:)-tcq9)*