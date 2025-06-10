# connection(_:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:)

**Framework**: Foundation  
**Kind**: method

Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, didSendBodyData bytesWritten: Int, totalBytesWritten: Int, totalBytesExpectedToWrite: Int)
```

#### Discussion

This method provides an estimate of the progress of a URL upload.

The value of `totalBytesExpectedToWrite` may change during the upload if the request needs to be retransmitted due to a lost connection or an authentication challenge from the server.

## Parameters

- `connection`: The connection sending the message.
- `bytesWritten`: The number of bytes written in the latest write.
- `totalBytesWritten`: The total number of bytes written for this connection.
- `totalBytesExpectedToWrite`: The number of bytes the connection expects to write.

## See Also

- [func connectionDidFinishLoading(NSURLConnection)](nsurlconnectiondatadelegate/connectiondidfinishloading(_:).md)
  Sent when a connection has finished loading successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didsendbodydata:totalbyteswritten:totalbytesexpectedtowrite:))*