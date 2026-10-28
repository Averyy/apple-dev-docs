# fetchWebAuthTokenCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The block to execute when the operation finishes.

**Availability**:
- iOS 9.2+ - Deprecated in 15.0
- iPadOS 9.2+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.11+ - Deprecated in 12.0
- tvOS 9.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use fetchWebAuthTokenResultBlock instead

## Declaration

```swift
var fetchWebAuthTokenCompletionBlock: ((String?, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^fetchWebAuthTokenCompletionBlock)(NSString *webAuthToken, NSError *operationError);
```

## Discussion

The closure returns no value and takes the following parameters:

- If the operation is successful, the web authentication token; otherwise, `nil`.
- An error that contains information about a problem, or `nil` if the system successfully fetches the token.

The operation executes this closure only once. You must provide a closure capable of executing on a background thread, so any tasks that require access to the main thread must dispatch accordingly.

## See Also

### Managing the Operation’s Configuration
- [var apiToken: String?](./apitoken.md)
  The API token that allows access to an app’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/fetchwebauthtokencompletionblock)*