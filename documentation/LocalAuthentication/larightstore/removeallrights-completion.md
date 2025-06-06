# removeAllRights(completion:)

**Framework**: Local Authentication  
**Kind**: method

Removes all rights associated with this client from the right store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllRights() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func removeAllRights() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func removeAllRights() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Removing rights also removes any resources stored along with the rights, such as secrets.

## Parameters

- `handler`: A completion handler to call when the removal operation completes.

## See Also

- [func removeRight(LAPersistedRight, completion: ((any Error)?) -> Void)](larightstore/removeright(_:completion:).md)
  Removes a right from the right store given an instance of that right.
- [func removeRight(forIdentifier: String, completion: ((any Error)?) -> Void)](larightstore/removeright(foridentifier:completion:).md)
  Removes a right from the right store given its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore/removeallrights(completion:))*