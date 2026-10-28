# URLSession.DelayedRequestDisposition

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The action to take on a delayed URL session task.

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
enum DelayedRequestDisposition
```

```c
enum NSURLSessionDelayedRequestDisposition : NSInteger;
```

## Overview

The values of this enumeration indicate how to handle a task with a delayed start time (as set with the [`earliestBeginDate`](../urlsessiontask/earliestbegindate.md) property). When the task is ready to start, it calls the [`urlSession(_:task:willBeginDelayedRequest:completionHandler:)`](../urlsessiontaskdelegate/urlsession%28_,task,willbegindelayedrequest,completionhandler%29.md) method of [`URLSessionTaskDelegate`](../urlsessiontaskdelegate.md). The implementation of this method must call the provided completion handler, passing in one case of this enumeration as the first argument. If the [`URLSession.DelayedRequestDisposition.useNewRequest`](./delayedrequestdisposition/usenewrequest.md) disposition is used for the first argument, the caller must also provide a new [`NSURLRequest`](../nsurlrequest.md) as the second argument.

## Topics

### Dispositions
- [URLSession.DelayedRequestDisposition.cancel](./delayedrequestdisposition/cancel.md)
  A disposition indicating that the task should be canceled.
- [URLSession.DelayedRequestDisposition.continueLoading](./delayedrequestdisposition/continueloading.md)
  A disposition indicating that the task should proceed with the original request.
- [URLSession.DelayedRequestDisposition.useNewRequest](./delayedrequestdisposition/usenewrequest.md)
  A disposition indicating that the task should use a new request to perform the network load.
### Initializers
- [init?(rawValue: Int)](./delayedrequestdisposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling delayed and waiting tasks
- [func urlSession(URLSession, task: URLSessionTask, willBeginDelayedRequest: URLRequest, completionHandler: (URLSession.DelayedRequestDisposition, URLRequest?) -> Void)](../urlsessiontaskdelegate/urlsession%28_,task,willbegindelayedrequest,completionhandler%29.md)
  Tells the delegate that a delayed URL session task will now begin loading.
- [func urlSession(URLSession, taskIsWaitingForConnectivity: URLSessionTask)](../urlsessiontaskdelegate/urlsession%28_,taskiswaitingforconnectivity%29.md)
  Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/delayedrequestdisposition)*