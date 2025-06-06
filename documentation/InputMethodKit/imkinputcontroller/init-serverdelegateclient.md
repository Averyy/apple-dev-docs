# init(server:delegate:client:)

**Framework**: InputMethodKit  
**Kind**: init

Initializes the input control by setting the delegate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(server: IMKServer!, delegate: Any!, client inputClient: Any!)
```

#### Return Value

The initialized input controller object.

#### Discussion

Methods in the [`IMKStateSetting`](imkstatesetting.md) and [`IMKMouseHandling`](imkmousehandling.md) protocols that are implemented by the delegate object always include a client parameter. Methods in the `IMKInputController` class do not need to take a client  because the `initWithServer:delegate:client:` method stores the client object you supply as an ivar when it initializes the `IMKInputController` object.

## Parameters

- `server`: The server object for the controller.
- `delegate`: The delegate object.
- `inputClient`: The client object that will send messages to the controller using the server object. The client object must confirm to the   protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/init(server:delegate:client:))*