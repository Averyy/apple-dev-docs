# requestAuthorization(completionHandler:)

**Framework**: SafetyKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to access Crash Detection information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
func requestAuthorization(completionHandler handler: @escaping @Sendable (SAAuthorizationStatus, (any Error)?) -> Void)
```

```swift
func requestAuthorization() async throws -> SAAuthorizationStatus
```

```objc
- (void) requestAuthorizationWithCompletionHandler:(void (^)(SAAuthorizationStatus status, NSError *error)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestAuthorization() async throws -> SAAuthorizationStatus
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method requests a person to authorize your app to receive Crash Detection events. Before requesting authorization, verify that your app already has authorization by verifying that [`authorizationStatus`](./authorizationstatus.md) is [`true`](../../Swift/true.md).

## Parameters

- `handler`: The completion handler invoked with the status of the authorization request.

## See Also

### Requesting authorization
- [var delegate: (any SACrashDetectionDelegate)?](./delegate.md)
  The object that receives Crash Detection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/requestauthorization(completionhandler:))*