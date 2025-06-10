# connection(_:didFailWithError:)

**Framework**: Foundation  
**Kind**: method

Sent when a connection fails to load its request successfully.

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
optional func connection(_ connection: NSURLConnection, didFailWithError error: any Error)
```

#### Discussion

Once the delegate receives this message, it will receive no further messages for `connection`.

## Parameters

- `connection`: The connection sending the message.
- `error`: An error object containing details of why the connection failed to load the request successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didfailwitherror:))*