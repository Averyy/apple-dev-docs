# PerformanceTestRequest

**Framework**: Retention Messaging API  
**Kind**: dictionary

The request object you provide for a performance test that contains an original transaction identifier.

**Availability**:
- Retention Messaging API 1.3+

## Declaration

```swift
object PerformanceTestRequest
```

#### Overview

To provide a transaction identifier for the purpose of performance testing, check that the transaction meets the following requirements:

- The transaction is for an active auto-renewable subscription.
- The transaction occurs in the sandbox environment.

## Properties

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of an In-App Purchase you initiate in the sandbox environment, to use as the purchase for this test.

## See Also

- [Initiate Performance Test](initiate-performance-test.md)
  Initiates a performance test of your Get Retention Message endpoint in the sandbox environment.
- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/performancetestrequest)*