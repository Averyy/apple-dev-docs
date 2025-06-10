# cancel()

**Framework**: Foundation  
**Kind**: method

Cancels an asynchronous load of a request.

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
func cancel()
```

#### Discussion

After this method is called, the connection makes no further delegate method calls. If you want to reattempt the connection, you should create a new connection object.

## See Also

- [init?(request: URLRequest, delegate: Any?)](nsurlconnection/init(request:delegate:).md)
  Returns an initialized URL connection and begins to load the data for the URL request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/cancel())*