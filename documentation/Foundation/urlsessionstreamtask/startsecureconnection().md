# startSecureConnection()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Completes any enqueued reads and writes, and establishes a secure connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startSecureConnection()
```

```objc
- (void) startSecureConnection;
```

## Discussion

Authentication callbacks are sent to the session’s delegate using the [`urlSession(_:task:didReceive:completionHandler:)`](../urlsessiontaskdelegate/urlsession%28_,task,didreceive,completionhandler%29.md) method.

## See Also

### Starting and stopping secure connections
- [func stopSecureConnection()](./stopsecureconnection%28%29.md)
  Completes any enqueued reads and writes, and closes the secure connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/startsecureconnection())*