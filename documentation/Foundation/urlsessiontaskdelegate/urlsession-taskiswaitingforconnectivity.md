# urlSession(_:taskIsWaitingForConnectivity:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, taskIsWaitingForConnectivity task: URLSessionTask)
```

#### Discussion

This method is called if the  [`waitsForConnectivity`](urlsessionconfiguration/waitsforconnectivity.md) property of [`URLSessionConfiguration`](urlsessionconfiguration.md) is `true`, and sufficient connectivity is unavailable. The delegate can use this opportunity to update the user interface; for example, by presenting an offline mode or a cellular-only mode.

This method is called, at most, once per task, and only if connectivity is initially unavailable. It is never called for background sessions because `waitsForConnectivity` is ignored for those sessions.

## Parameters

- `session`: The session that contains the waiting task.
- `task`: The task that is waiting for a change in connectivity.

## See Also

- [func urlSession(URLSession, task: URLSessionTask, willBeginDelayedRequest: URLRequest, completionHandler: (URLSession.DelayedRequestDisposition, URLRequest?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:willbegindelayedrequest:completionhandler:).md)
  Tells the delegate that a delayed URL session task will now begin loading.
- [URLSession.DelayedRequestDisposition](urlsession/delayedrequestdisposition.md)
  The action to take on a delayed URL session task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:taskiswaitingforconnectivity:))*