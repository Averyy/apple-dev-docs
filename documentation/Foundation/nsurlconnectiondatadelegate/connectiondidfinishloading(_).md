# connectionDidFinishLoading(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when a connection has finished loading successfully.

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
optional func connectionDidFinishLoading(_ connection: NSURLConnection)
```

```objc
- (void) connectionDidFinishLoading:(NSURLConnection *) connection;
```

#### Discussion

The delegate will receive no further messages for `connection`.

## Parameters

- `connection`: The connection sending the message.

## See Also

### Receiving Connection Progress
- [func connection(NSURLConnection, didSendBodyData: Int, totalBytesWritten: Int, totalBytesExpectedToWrite: Int)](./connection%28_,didsendbodydata,totalbyteswritten,totalbytesexpectedtowrite%29.md)
  Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connectiondidfinishloading(_:))*