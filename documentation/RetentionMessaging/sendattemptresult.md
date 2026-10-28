# sendAttemptResult

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The success or error information the App Store server records when it attempts to send an App Store server notification to your server.

**Availability**:
- Retention Messaging API 1.3+

## Declaration

```
string sendAttemptResult
```

## Possible Values

- `SUCCESS`: The App Store server received a success response when it sent the notification to your server.
- `CIRCULAR_REDIRECT`: The App Store server detected a continual redirect. Check your server’s redirects for a circular redirect loop.
- `INVALID_RESPONSE`: The App Store server received an invalid response from your server.
- `NO_RESPONSE`: The App Store server didn’t receive a valid HTTP response from your server.
- `OTHER`: Another error occurred that prevented your server from receiving the notification.
- `PREMATURE_CLOSE`: The App Store server’s connection to your server was closed while the send was in progress.
- `SOCKET_ISSUE`: A network error caused the notification attempt to fail.
- `TIMED_OUT`: The App Store server didn’t get a response from your server and timed out. Check that your server isn’t processing messages in line.
- `TLS_ISSUE`: The App Store server couldn’t establish a TLS session or validate your certificate. Check that your server has a valid certificate and supports Transport Layer Security (TLS) protocol 1.2 or later.
- `UNSUCCESSFUL_HTTP_RESPONSE_CODE`: The App Store server didn’t receive an `HTTP 200` response from your server.
- `UNSUPPORTED_CHARSET`: The App Store server doesn’t support the supplied charset.

## Discussion

This value describes the success or error the server encountered on its attempt to send the notification to your server as part of a performance test.

## See Also

### Performance testing
- [object PerformanceTestConfig](./performancetestconfig.md)
  An object that enumerates the test configuration parameters.
- [object PerformanceTestRequest](./performancetestrequest.md)
  The request object you provide for a performance test that contains an original transaction identifier.
- [object PerformanceTestResponse](./performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResponseTimes](./performancetestresponsetimes.md)
  An object that describes test response times.
- [object PerformanceTestResultResponse](./performancetestresultresponse.md)
  An object the API returns that describes the performance test results.
- [type PerformanceTestStatus](./performanceteststatus.md)
  The status of the performance test.
- [object Failures](./failures.md)
  A map of server-to-server notification failure reasons and counts that represent the number of failures during a performance test.
- [type requestId](./requestid.md)
  The identifier of the performance test request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/sendattemptresult)*