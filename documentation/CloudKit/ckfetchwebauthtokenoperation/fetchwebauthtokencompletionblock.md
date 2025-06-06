# fetchWebAuthTokenCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The block to execute when the operation finishes.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var fetchWebAuthTokenCompletionBlock: ((String?, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- If the operation is successful, the web authentication token; otherwise, `nil`.
- An error that contains information about a problem, or `nil` if the system successfully fetches the token.

The operation executes this closure only once. Your closure must be capable of executing on a background thread, so any tasks that require access to the main thread must dispatch accordingly.

## See Also

- [var apiToken: String?](ckfetchwebauthtokenoperation/apitoken.md)
  The API token that allows access to an app’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/fetchwebauthtokencompletionblock)*