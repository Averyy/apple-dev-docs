# unregister()

**Framework**: Service Management  
**Kind**: method  
**Role**: Instance Method

Unregisters the service so the system no longer launches it.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func unregister() throws
```

```objc
- (BOOL) unregisterAndReturnError:(NSError **) error;
```

#### Discussion

This is the opposite operation of [`register()`](./register%28%29.md).

If the service corresponds to a LoginItem, LaunchAgent, or LaunchDaemon and the service is currently running it, the system terminates it. If the service corresponds to the main application, it continues running, but becomes unregistered to prevent future launches at login.

If the service is already unregistered, this method returns [`kSMErrorJobNotFound`](../ksmerrorjobnotfound.md).

## See Also

### Registering services
- [func register() throws](./register%28%29.md)
  Registers the service so it can begin launching subject to user approval.
- [func unregister(completionHandler: ((any Error)?) -> Void)](./unregister%28completionhandler%29.md)
  Unregisters the service so the system no longer launches it and calls a completion handler you provide with the resulting error value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/unregister())*