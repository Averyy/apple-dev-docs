# start(delegate:subscriptionRange:with:)

**Framework**: CarKey  
**Kind**: method

Creates and returns a new session object to access the provisioned vehicles.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
class func start(delegate: any CarKeyRemoteControlSessionDelegate, subscriptionRange subscriptionFunctionIDRange: ClosedRange<Int>? = nil, with delegateCallbackQueue: DispatchQueue? = nil) async throws -> CarKeyRemoteControlSession
```

#### Return Value

A new session object.

#### Discussion

This method creates a new session object each time you call it. You can have only one active session at a time. If you call this method while a session is already active, the method waits until the previous session becomes invalid before returning the new session. The session object gives you access to the vehicles that your company makes and that the owner added to their Apple Wallet.

## Parameters

- `delegate`: The object you use to receive data from the   vehicle and handle connection issues. You must specify this   object at session-creation time, and can only change it by   creating a new session. This object must adopt the    protocol.
- `subscriptionFunctionIDRange`: The range of function IDs your   app supports for the current session. Each vehicle feature you   can control remotely has an associated function identifier code.   Use this parameter to limit the features accessible to the current   person. For example, you might include a subset of features to   limit the actions of someone who isn’t the vehicle’s primary owner.
- `delegateCallbackQueue`: The queue on which to execute the methods   of your delegate object. If you specify  , CarKey creates a new   serial dispatch queue for you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrol/start(delegate:subscriptionrange:with:))*