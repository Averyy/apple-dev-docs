# saveRight(_:identifier:secret:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Saves a right to a persistent store along with secret data you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func saveRight(_ right: LARight, identifier: String, secret: Data, completion handler: @escaping @Sendable (LAPersistedRight?, (any Error)?) -> Void)
```

```swift
func saveRight(_ right: LARight, identifier: String, secret: Data) async throws -> LAPersistedRight
```

```objc
- (void) saveRight:(LARight *) right identifier:(NSString *) identifier secret:(NSData *) secret completion:(void (^)(LAPersistedRight *, NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func saveRight(_ right: LARight, identifier: String, secret: Data) async throws -> LAPersistedRight
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `right`: The right to store.
- `identifier`: A unique identifier for the right.
- `secret`: Secret data that’s stored with the right.
- `handler`: A completion handler to call when the save operation completes.

  - **`right`**: The persisted form of the right that the save operation stores.
  - **`error`**: An error object that indicates why the `right` parameter is `nil`, or `nil` if the right parameter is non-`nil`.

## See Also

### Storing rights
- [func saveRight(LARight, identifier: String, completion: (LAPersistedRight?, (any Error)?) -> Void)](./saveright%28_,identifier,completion%29.md)
  Saves a right to a persistent right store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore/saveright(_:identifier:secret:completion:))*