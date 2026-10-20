# loadData(completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Retrieves data stored in a secret.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func loadData(completion handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
var rawData: Data { get async throws }
```

```objc
- (void) loadDataWithCompletion:(void (^)(NSData *, NSError *)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> var rawData: Data { get async throws }
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `handler`: A completion handler that provides the data stored in a secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lasecret/loaddata(completion:))*