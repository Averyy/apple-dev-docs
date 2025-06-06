# unregister()

**Framework**: Service Management  
**Kind**: method

Unregisters the service so the system no longer launches it.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func unregister() throws
```

#### Discussion

This is the opposite operation of [`register()`](smappservice/register().md).

If the service corresponds to a LoginItem, LaunchAgent, or LaunchDaemon and the service is currently running it, the system terminates it. If the service corresponds to the main application, it continues running, but becomes unregistered to prevent future launches at login.

If the service is already unregistered, this method returns [`kSMErrorJobNotFound`](ksmerrorjobnotfound.md).

## See Also

- [func register() throws](smappservice/register.md)
  Registers the service so it can begin launching subject to user approval.
- [func unregister(completionHandler: ((any Error)?) -> Void)](smappservice/unregister(completionhandler:).md)
  Unregisters the service so the system no longer launches it and calls a completion handler you provide with the resulting error value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/unregister())*