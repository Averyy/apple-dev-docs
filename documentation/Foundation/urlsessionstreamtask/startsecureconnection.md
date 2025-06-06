# startSecureConnection()

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

Authentication callbacks are sent to the session’s delegate using the [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method.

## See Also

- [func stopSecureConnection()](urlsessionstreamtask/stopsecureconnection.md)
  Completes any enqueued reads and writes, and closes the secure connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/startsecureconnection())*