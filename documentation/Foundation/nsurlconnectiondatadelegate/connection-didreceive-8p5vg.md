# connection(_:didReceive:)

**Framework**: Foundation  
**Kind**: method

Sent as a connection loads data incrementally.

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
optional func connection(_ connection: NSURLConnection, didReceive data: Data)
```

#### Discussion

This method provides the only way for an asynchronous delegate to retrieve the loaded data. It is the responsibility of the delegate to retain or copy this data as it is delivered.

## Parameters

- `connection`: The connection sending the message.
- `data`: The newly available data. The delegate should concatenate the contents of each   object delivered to build up the complete data for a URL load.

## See Also

- [func connection(NSURLConnection, didReceive: URLResponse)](nsurlconnectiondatadelegate/connection(_:didreceive:)-8t66w.md)
  Sent when the connection has received sufficient data to construct the URL response for its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8p5vg)*