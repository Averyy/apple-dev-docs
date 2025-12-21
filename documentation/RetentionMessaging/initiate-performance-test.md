# Initiate Performance Test

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Initiates a performance test

**Availability**:
- Retention Messaging 1.3+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

Call this endpoint to start a new performance test. The service returns a response that includes a [`PerformanceTestConfig`](performancetestconfig.md) object that describes the testing parameters and a `requestId` you can use to request test results.

## Request Body

The request body that includes a [`PerformanceTestRequest`](performancetestrequest.md) object that specifies the transaction identifier of an In-App Purchase to use to as the purchase for this test.

## See Also

- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/initiate-performance-test)*