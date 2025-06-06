# unregister(completionHandler:)

**Framework**: Service Management  
**Kind**: method

Unregisters the service so the system no longer launches it and calls a completion handler you provide with the resulting error value.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func unregister() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func unregister() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func unregister() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `handler`: A completion handler to call with the result of the unregistration operation. Upon an unsuccessful return, the handler contains a new   object describing the error. Upon successful return, this argument is  .

## See Also

- [func register() throws](smappservice/register.md)
  Registers the service so it can begin launching subject to user approval.
- [func unregister() throws](smappservice/unregister.md)
  Unregisters the service so the system no longer launches it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/unregister(completionhandler:))*