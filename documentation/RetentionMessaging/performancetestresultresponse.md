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

## Properties

- `config` (PerformanceTestConfig) *(required)*: A [`PerformanceTestConfig`](performancetestconfig.md) object that enumerates the test parameters.
- `failures` (Failures) *(required)*: A [`Failures`](failures.md) object that represents a map of server-to-server notification failure reasons and counts that represent the number of failures encountered during the performance test.
- `numPending` (int32) *(required)*: An integer that describes the number of pending requests in the performance test.
- `responseTimes` (PerformanceTestResponseTimes) *(required)*: A [`PerformanceTestResponseTimes`](performancetestresponsetimes.md) object that enumerates the response times measured during the test.
- `result` (PerformanceTestStatus) *(required)*: A [`PerformanceTestStatus`](performanceteststatus.md) object that describes the overall result of the test.
- `successRate` (int32) *(required)*: An integer that describes he success rate percentage of the performance test.
- `target` (string) *(required)*: The target URL for the performance test.

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