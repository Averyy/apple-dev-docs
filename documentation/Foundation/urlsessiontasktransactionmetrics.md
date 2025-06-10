# URLSessionTaskTransactionMetrics

**Framework**: Foundation  
**Kind**: class

An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.

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
class URLSessionTaskTransactionMetrics
```

#### Overview

Each [`URLSessionTaskTransactionMetrics`](urlsessiontasktransactionmetrics.md) object consists of a [`request`](urlsessiontasktransactionmetrics/request.md) and [`response`](urlsessiontasktransactionmetrics/response.md) property, corresponding to the request and response of the corresponding task. It also contains temporal metrics, starting with [`fetchStartDate`](urlsessiontasktransactionmetrics/fetchstartdate.md) and ending with [`responseEndDate`](urlsessiontasktransactionmetrics/responseenddate.md), as well as other characteristics like [`networkProtocolName`](urlsessiontasktransactionmetrics/networkprotocolname.md) and [`resourceFetchType`](urlsessiontasktransactionmetrics/resourcefetchtype.md).

##### Understanding Temporal Metrics

The figure below shows the sequence of events for a URL session task, which correspond to the temporal metrics captured by [`URLSessionTaskTransactionMetrics`](urlsessiontasktransactionmetrics.md).

![Diagram showing the temporal metrics for a URL session task. When a task starts, it performs a DNS lookup and then starts a connection. If the connection is encrypted, the user agent starts a TLS security handshake to secure the connection. After the connection to the server is established, the user agent requests the specified resource, and receives a response.](https://docs-assets.developer.apple.com/published/fe43fa65ab15aa2971fae2fab53e1a4f/media-3162616%402x.png)

For all metrics with a start and end date, if an aspect of the task was not completed, then its corresponding end date metric is `nil`. This can happen if name lookup begins, but the operation either times out, fails, or the client cancels the task before the name can be resolved. In this case, the [`domainLookupEndDate`](urlsessiontasktransactionmetrics/domainlookupenddate.md) property is `nil`, along with all metrics for aspects that occurred afterwards.

##### Measuring Tasks Using Icloud Private Relay

iCloud Private Relay can change the timing and sequence of events for your tasks by sending requests through a set of privacy proxies. All tasks that use iCloud Private Relay set the [`isProxyConnection`](urlsessiontasktransactionmetrics/isproxyconnection.md) property in their transaction metrics. In this case, the [`remoteAddress`](urlsessiontasktransactionmetrics/remoteaddress.md) property contains the address of the proxy, and not the origin server.

Tasks to different hosts can reuse the same transport connection, just like how tasks can already share a connection when using HTTP/2. In these cases, a proxied task may not report any [`secureConnectionStartDate`](urlsessiontasktransactionmetrics/secureconnectionstartdate.md) or [`secureConnectionEndDate`](urlsessiontasktransactionmetrics/secureconnectionenddate.md).

## Topics

### Accessing request and response
- [var request: URLRequest](urlsessiontasktransactionmetrics/request.md)
  The transaction request.
- [var response: URLResponse?](urlsessiontasktransactionmetrics/response.md)
  The transaction response.
### Accessing temporal metrics
- [var fetchStartDate: Date?](urlsessiontasktransactionmetrics/fetchstartdate.md)
  The time when the task started fetching the resource, from the server or locally.
- [var domainLookupStartDate: Date?](urlsessiontasktransactionmetrics/domainlookupstartdate.md)
  The time immediately before the task started the name lookup for the resource.
- [var domainLookupEndDate: Date?](urlsessiontasktransactionmetrics/domainlookupenddate.md)
  The time after the name lookup was completed.
- [var connectStartDate: Date?](urlsessiontasktransactionmetrics/connectstartdate.md)
  The time immediately before the task started establishing a TCP connection to the server.
- [var secureConnectionStartDate: Date?](urlsessiontasktransactionmetrics/secureconnectionstartdate.md)
  The time immediately before the task started the TLS security handshake to secure the current connection.
- [var secureConnectionEndDate: Date?](urlsessiontasktransactionmetrics/secureconnectionenddate.md)
  The time immediately after the security handshake completed.
- [var connectEndDate: Date?](urlsessiontasktransactionmetrics/connectenddate.md)
  The time immediately after the task finished establishing the connection to the server.
- [var requestStartDate: Date?](urlsessiontasktransactionmetrics/requeststartdate.md)
  The time immediately before the task started requesting the resource, regardless of whether it is retrieved from the server or local resources.
- [var requestEndDate: Date?](urlsessiontasktransactionmetrics/requestenddate.md)
  The time immediately after the task finished requesting the resource, regardless of whether it was retrieved from the server or local resources.
- [var responseStartDate: Date?](urlsessiontasktransactionmetrics/responsestartdate.md)
  The time immediately after the task received the first byte of the response from the server or from local resources.
- [var responseEndDate: Date?](urlsessiontasktransactionmetrics/responseenddate.md)
  The time immediately after the task received the last byte of the resource.
### Accessing data transfer metrics
- [var countOfRequestBodyBytesBeforeEncoding: Int64](urlsessiontasktransactionmetrics/countofrequestbodybytesbeforeencoding.md)
  The size of the upload body data, file, or stream, in bytes.
- [var countOfRequestBodyBytesSent: Int64](urlsessiontasktransactionmetrics/countofrequestbodybytessent.md)
  The number of bytes transferred for the request body.
- [var countOfRequestHeaderBytesSent: Int64](urlsessiontasktransactionmetrics/countofrequestheaderbytessent.md)
  The number of bytes transferred for the request header.
- [var countOfResponseBodyBytesAfterDecoding: Int64](urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding.md)
  The size of data delivered to your delegate or completion handler.
- [var countOfResponseBodyBytesReceived: Int64](urlsessiontasktransactionmetrics/countofresponsebodybytesreceived.md)
  The number of bytes transferred for the response body.
- [var countOfResponseHeaderBytesReceived: Int64](urlsessiontasktransactionmetrics/countofresponseheaderbytesreceived.md)
  The number of bytes transferred for the response header.
### Accessing transaction characteristics
- [var networkProtocolName: String?](urlsessiontasktransactionmetrics/networkprotocolname.md)
  The network protocol used to fetch the resource.
- [var remoteAddress: String?](urlsessiontasktransactionmetrics/remoteaddress.md)
  The IP address string of the remote interface for the connection.
- [var remotePort: Int?](urlsessiontasktransactionmetrics/remoteport.md)
  The port number of the remote interface for the connection.
- [var localAddress: String?](urlsessiontasktransactionmetrics/localaddress.md)
  The IP address string of the local interface for the connection.
- [var localPort: Int?](urlsessiontasktransactionmetrics/localport.md)
  The port number of the local interface for the connection.
- [var negotiatedTLSCipherSuite: tls_ciphersuite_t?](urlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [var negotiatedTLSProtocolVersion: tls_protocol_version_t?](urlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.
- [var isCellular: Bool](urlsessiontasktransactionmetrics/iscellular.md)
  A Boolean value that indicates whether the connection operates over a cellular interface.
- [var isExpensive: Bool](urlsessiontasktransactionmetrics/isexpensive.md)
  A Boolean value that indicates whether the connection operates over an expensive interface.
- [var isConstrained: Bool](urlsessiontasktransactionmetrics/isconstrained.md)
  A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [var isProxyConnection: Bool](urlsessiontasktransactionmetrics/isproxyconnection.md)
  A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [var isReusedConnection: Bool](urlsessiontasktransactionmetrics/isreusedconnection.md)
  A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [var isMultipath: Bool](urlsessiontasktransactionmetrics/ismultipath.md)
  A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [var resourceFetchType: URLSessionTaskMetrics.ResourceFetchType](urlsessiontasktransactionmetrics/resourcefetchtype.md)
  A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [URLSessionTaskMetrics.ResourceFetchType](urlsessiontaskmetrics/resourcefetchtype.md)
  The manner in which a resource is fetched.
- [var domainResolutionProtocol: URLSessionTaskMetrics.DomainResolutionProtocol](urlsessiontasktransactionmetrics/domainresolutionprotocol.md)
- [URLSessionTaskMetrics.DomainResolutionProtocol](urlsessiontaskmetrics/domainresolutionprotocol.md)
### Creating transaction metrics
- [init()](urlsessiontasktransactionmetrics/init.md)
  Creates a transaction metrics instance.
- [class func new() -> Self](urlsessiontasktransactionmetrics/new.md)
  Creates a new transaction metrics instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var transactionMetrics: [URLSessionTaskTransactionMetrics]](urlsessiontaskmetrics/transactionmetrics.md)
  An array of metrics for each individual request-response transaction made during the execution of the task.
- [var taskInterval: DateInterval](urlsessiontaskmetrics/taskinterval.md)
  The time interval between when a task is instantiated and when the task is completed.
- [var redirectCount: Int](urlsessiontaskmetrics/redirectcount.md)
  The number of redirects that occurred during the execution of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics)*