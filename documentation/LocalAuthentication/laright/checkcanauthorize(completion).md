# checkCanAuthorize(completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Checks whether the right has permission to perform authorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func checkCanAuthorize(completion handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func checkCanAuthorize() async throws
```

```objc
- (void) checkCanAuthorizeWithCompletion:(void (^)(NSError *error)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func checkCanAuthorize() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `handler`: A completion handler called when the authorization check finishes.

  - **`error`**: If `nil`, the right can be authorized.

## See Also

### Monitoring authorization status
- [var state: LARight.State](./state-swift.property.md)
  The current authorization state for a right.
- [LARight.State](./state-swift.enum.md)
  The possible states for a right during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/checkcanauthorize(completion:))*