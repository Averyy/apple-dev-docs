# removeRight(forIdentifier:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Removes a right from the right store given its unique identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func removeRight(forIdentifier identifier: String, completion handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeRight(forIdentifier identifier: String) async throws
```

```objc
- (void) removeRightForIdentifier:(NSString *) identifier completion:(void (^)(NSError *error)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func removeRight(forIdentifier identifier: String) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Removing a right also removes any resources stored along with the right, such as secrets.

## Parameters

- `identifier`: The identifier for the right to remove.
- `handler`: A completion handler to call when the removal operation completes.

  - **`error`**: An error object that indicates why the removal operation failed, or `nil` if it succeeded.

## See Also

### Removing stored rights
- [func removeRight(LAPersistedRight, completion: ((any Error)?) -> Void)](./removeright%28_,completion%29.md)
  Removes a right from the right store given an instance of that right.
- [func removeAllRights(completion: ((any Error)?) -> Void)](./removeallrights%28completion%29.md)
  Removes all rights associated with this client from the right store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore/removeright(foridentifier:completion:))*