# unregister(completionHandler:)

**Framework**: Service Management  
**Kind**: method  
**Role**: Instance Method

Unregisters the service so the system no longer launches it and calls a completion handler you provide with the resulting error value.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func unregister(completionHandler handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func unregister() async throws
```

```objc
- (void) unregisterWithCompletionHandler:(void (^)(NSError *error)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func unregister() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `handler`: A completion handler to call with the result of the unregistration operation. Upon an unsuccessful return, the handler contains a new [`NSError`](../../Foundation/nserror.md) object describing the error. Upon successful return, this argument is `NULL`.

## See Also

### Registering services
- [func register() throws](./register%28%29.md)
  Registers the service so it can begin launching subject to user approval.
- [func unregister() throws](./unregister%28%29.md)
  Unregisters the service so the system no longer launches it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/unregister(completionhandler:))*