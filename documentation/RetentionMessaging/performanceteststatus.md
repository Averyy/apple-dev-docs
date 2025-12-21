# PerformanceTestStatus

**Framework**: Retention Messaging API  
**Kind**: typealias

The status of the performance test.

**Availability**:
- Retention Messaging 1.3+

## Declaration

```swift
string PerformanceTestStatus
```

#### Discussion

- Possible Values - PENDING: The test is still pending.
- PASS:  The test passed. For additional details, see the specific [`PerformanceTestResponse`](performancetestresponse.md) results.
- FAIL: The test failed. For additional details, see the specific [`PerformanceTestResponse`](performancetestresponse.md) results.

## See Also

- [object PerformanceTestConfig](performancetestconfig.md)
  An object that enumerates the test configuration parameters.
- [object PerformanceTestRequest](performancetestrequest.md)
  The object you provide to a performance test request that contains the test’s transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResponseTimes](performancetestresponsetimes.md)
  An object that describes test response times.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.
- [object Failures](failures.md)
  A map of server-to-server notification failure reasons and counts that represent the number of failures during a performance test.
- [type sendAttemptResult](sendattemptresult.md)
  The success or error information the App Store server records when it attempts to send an App Store server notification to your server.
- [type requestId](requestid.md)
  The identifier of the performance test request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/performanceteststatus)*