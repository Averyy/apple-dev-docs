# authorize(localizedReason:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Performs an authorization on the right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func authorize(localizedReason: String, completion handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func authorize(localizedReason: String) async throws
```

```objc
- (void) authorizeWithLocalizedReason:(NSString *) localizedReason completion:(void (^)(NSError *error)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func authorize(localizedReason: String) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `localizedReason`: A reason for the authorization that the system displays to the user.
- `handler`: A completion handler called at the end of the authorization process.

  - **`error`**: If `nil`, the authorization is successful. Otherwise, the error contains information about the failure reason.

## See Also

### Authorizing a right
- [init()](./init%28%29.md)
  Creates a right using the default authorization requirements.
- [init(requirement: LAAuthenticationRequirement)](./init%28requirement%29.md)
  Creates a right with the authentication requirements you supply.
- [var tag: Int](./tag.md)
  An integer you use to identify a right.
- [func authorize(localizedReason: String, in: LAPresentationContext, completion: ((any Error)?) -> Void)](./authorize%28localizedreason,in,completion%29.md)
  Performs an authorization on the right with a window context you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/authorize(localizedreason:completion:))*