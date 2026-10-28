# SLRequestMethod

**Framework**: Social  
**Kind**: enum  
**Role**: Enumeration

Indicates the request method used in the request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
enum SLRequestMethod
```

```c
enum SLRequestMethod : NSInteger;
```

## Overview

Use this constant to set the [`requestMethod`](./slrequest/requestmethod.md) property. The type of request to use depends on the target service. For links to documentation for the supported services, see Table 1 in [`SLRequest`](./slrequest.md).

## Topics

### Constants
- [SLRequestMethod.GET](./slrequestmethod/get.md)
  Requests information from the specified resource.
- [SLRequestMethod.POST](./slrequestmethod/post.md)
  Submits data to be processed.
- [SLRequestMethod.DELETE](./slrequestmethod/delete.md)
  Deletes the specified resource.
- [SLRequestMethod.PUT](./slrequestmethod/put.md)
  Uses a PUT request to submit the data.
### Initializers
- [init?(rawValue: Int)](./slrequestmethod/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Request Details
- [func preparedURLRequest() -> URLRequest!](./slrequest/preparedurlrequest%28%29.md)
  Returns an authorized URL request that can be sent using an [`NSURLConnection`](../Foundation/nsurlconnection.md) object.
- [var requestMethod: SLRequestMethod](./slrequest/requestmethod.md)
  The method to use for this request.
- [var url: URL!](./slrequest/url.md)
  The destination URL for this request.
- [var parameters: [AnyHashable : Any]!](./slrequest/parameters.md)
  The parameters for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequestmethod)*