# PerformanceTestConfig

**Framework**: Retention Messaging API  
**Kind**: dictionary

An object that enumerates the test configuration parameters.

**Availability**:
- Retention Messaging API 1.3+

## Declaration

```swift
object PerformanceTestConfig
```

#### Overview

The [`Initiate Performance Test`](initiate-performance-test.md) endpoint returns the `PerformanceTestConfig` object in the [`PerformanceTestResponse`](performancetestresponse.md) response.

When you call the [`Initiate Performance Test`](initiate-performance-test.md) endpoint to start a performance test, the test sends multiple requests and runs for a period of time. To calculate the time when the test concludes, add the `totalDuration` to the time, in milliseconds, you initiated the test.

## Properties

- `maxConcurrentRequests` (int64) *(required)*: The maximum number of concurrent requests the API allows.
- `responseTimeThreshold` (int64) *(required)*: The maximum time your server has to respond when the system calls your `Get Retention Message` endpoint in the sandbox environment.
- `successRateThreshold` (int32) *(required)*: The success rate threshold percentage.
- `totalDuration` (int64) *(required)*: The total duration of the test in milliseconds.
- `totalRequests` (integer) *(required)*: The total number of requests to make during the test.

## See Also

- [object PerformanceTestRequest](performancetestrequest.md)
  The request object you provide for a performance test that contains an original transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResponseTimes](performancetestresponsetimes.md)
  An object that describes test response times.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.
- [type PerformanceTestStatus](performanceteststatus.md)
  The status of the performance test.
- [object Failures](failures.md)
  A map of server-to-server notification failure reasons and counts that represent the number of failures during a performance test.
- [type sendAttemptResult](sendattemptresult.md)
  The success or error information the App Store server records when it attempts to send an App Store server notification to your server.
- [type requestId](requestid.md)
  The identifier of the performance test request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/performancetestconfig)*