# PerformanceTestResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

The performance test response object.

**Availability**:
- Retention Messaging API 1.3+

## Declaration

```swift
object PerformanceTestResponse
```

#### Overview

Use the `requestId` to get the test results, by calling [`Get Performance Test Results`](get-performance-test-results.md).

## Properties

- `config` (PerformanceTestConfig) *(required)*: The performance test configuration object.
- `requestId` (requestId) *(required)*: The performance test request identifier.

## See Also

- [Initiate Performance Test](initiate-performance-test.md)
  Initiates a performance test of your Get Retention Message endpoint in the sandbox environment.
- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.
- [object PerformanceTestRequest](performancetestrequest.md)
  The request object you provide for a performance test that contains an original transaction identifier.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/performancetestresponse)*