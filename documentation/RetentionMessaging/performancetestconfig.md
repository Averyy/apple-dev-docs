# PerformanceTestConfig

**Framework**: Retention Messaging API  
**Kind**: dictionary

An object that enumerates the test configuration parameters.

**Availability**:
- Retention Messaging 1.3+

## Declaration

```swift
object PerformanceTestConfig
```

## Properties

- `maxConcurrentRequests` (int64) *(required)*: The maximum number of concurrent requests the API allows.
- `responseTimeThreshold` (int64) *(required)*: The response time threshold in milliseconds.
- `successRateThreshold` (int32) *(required)*: The success rate threshold percentage.
- `totalDuration` (int64) *(required)*: The total duration of the test in milliseconds.
- `totalRequests` (integer) *(required)*: The total number of requests to make during the test.

## See Also

- [object PerformanceTestRequest](performancetestrequest.md)
  The object you provide to a performance test request that contains the test’s transaction identifier.
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