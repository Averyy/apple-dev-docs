# stopSecureConnection()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Completes any enqueued reads and writes, and closes the secure connection.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: TLS cannot be disabled once it is enabled

## Declaration

```swift
func stopSecureConnection()
```

```objc
- (void) stopSecureConnection;
```

## See Also

### Starting and stopping secure connections
- [func startSecureConnection()](./startsecureconnection%28%29.md)
  Completes any enqueued reads and writes, and establishes a secure connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/stopsecureconnection())*