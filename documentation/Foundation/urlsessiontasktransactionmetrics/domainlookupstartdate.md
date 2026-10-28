# domainLookupStartDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time immediately before the task started the name lookup for the resource.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var domainLookupStartDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * domainLookupStartDate;
```

## Discussion

This value will be `nil` if a persistent connection was used, or if the resource was retrieved from local resources.

## See Also

### Accessing temporal metrics
- [var fetchStartDate: Date?](./fetchstartdate.md)
  The time when the task started fetching the resource, from the server or locally.
- [var domainLookupEndDate: Date?](./domainlookupenddate.md)
  The time after the name lookup was completed.
- [var connectStartDate: Date?](./connectstartdate.md)
  The time immediately before the task started establishing a TCP connection to the server.
- [var secureConnectionStartDate: Date?](./secureconnectionstartdate.md)
  The time immediately before the task started the TLS security handshake to secure the current connection.
- [var secureConnectionEndDate: Date?](./secureconnectionenddate.md)
  The time immediately after the security handshake completed.
- [var connectEndDate: Date?](./connectenddate.md)
  The time immediately after the task finished establishing the connection to the server.
- [var requestStartDate: Date?](./requeststartdate.md)
  The time immediately before the task started requesting the resource, regardless of whether it is retrieved from the server or local resources.
- [var requestEndDate: Date?](./requestenddate.md)
  The time immediately after the task finished requesting the resource, regardless of whether it was retrieved from the server or local resources.
- [var responseStartDate: Date?](./responsestartdate.md)
  The time immediately after the task received the first byte of the response from the server or from local resources.
- [var responseEndDate: Date?](./responseenddate.md)
  The time immediately after the task received the last byte of the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/domainlookupstartdate)*