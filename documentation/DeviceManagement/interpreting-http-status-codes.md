# Interpreting HTTP status codes

**Framework**: Device Management

Interpret error codes the API might return when executing a request.

#### Overview

An error code indicates the type of error that occurred while executing a request. These are the possible values for the `status` member in an [`Error`](error.md) object:

| Code | Name | Description |
| --- | --- | --- |
| 200 | OK | The request was successful; no errors or faults. |
| 201 | Created | Creation request was successful. |
| 202 | Accepted | Although the modification request was acceptable, it may not have completed. |
| 204 | No Content | Modification was successful, but there’s no content in the response. |
| 301 | Moved Permanently | Content may be available at a different URL. |
| 302 | Found | Content definitely available at a specific URL. |
| 400 | Bad Request | The request wasn’t accepted as formed. |
| 401 | Unauthorized | The request wasn’t accepted because its authorization is missing or invalid due to an issue with the developer token. |
| 403 | Forbidden | The request wasn’t accepted due to an issue with the user token or because it’s using incorrect authentication. |
| 404 | Not Found | The requested resource doesn’t exist. |
| 405 | Method Not Allowed | Can’t use specified method for the request. |
| 409 | Conflict | Couldn’t process modification or creation request because there’s a conflict with the current state of the resource. |
| 413 | Payload Too Large | The body of the request is too large. |
| 414 | URI Too Long | Won’t process the request because the URI is too long. |
| 429 | Too Many Requests | The user has made too many requests. See [`Limit request rate`](generating-developer-tokens#Limit-request-rate.md). |
| 500 | Internal Server Error | There’s an error processing the request. |
| 501 | Not Implemeneted | Endpoint is currently unavailable and reserved for future use. |
| 503 | Service Unavailable | The service is currently unavailable to process requests. |

## Topics

### Related Objects
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.

## See Also

- [object Error](error.md)
  Information about an error that occurred while processing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/interpreting-http-status-codes)*