# PerformanceTestResultResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

An object the API returns that describes the performance test results.

**Availability**:
- Retention Messaging 1.3+

## Declaration

```swift
object PerformanceTestResultResponse
```

##### Discussion

This object is the response the [`Get Performance Test Results`](get-performance-test-results.md) API call returns. To initiate a performance test, call [`Initiate Performance Test`](initiate-performance-test.md).

## See Also

- [object PerformanceTestConfig](performancetestconfig.md)
  An object that enumerates the test configuration parameters.
- [object PerformanceTestRequest](performancetestrequest.md)
  The object you provide to a performance test request that contains the test’s transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResponseTimes](performancetestresponsetimes.md)
  An object that describes test response times.
- [type PerformanceTestStatus](performanceteststatus.md)
  The status of the performance test.
- [object Failures](failures.md)
  A map of server-to-server notification failure reasons and counts that represent the number of failures during a performance test.
- [type sendAttemptResult](sendattemptresult.md)
  The success or error information the App Store server records when it attempts to send an App Store server notification to your server.
- [type requestId](requestid.md)
  The identifier of the performance test request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/performancetestresultresponse)*