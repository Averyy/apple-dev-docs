# getPendingTaskRequests(completionHandler:)

**Framework**: Background Tasks  
**Kind**: method

Request a list of unexecuted scheduled task requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func pendingTaskRequests() async -> [BGTaskRequest]
```

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func pendingTaskRequests() async -> [BGTaskRequest]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func pendingTaskRequests() async -> [BGTaskRequest]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The objects passed in the array are copies of the existing requests. Changing the attributes of a request has no effect. To change the attributes submit a new task request using  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/getpendingtaskrequests(completionhandler:))*