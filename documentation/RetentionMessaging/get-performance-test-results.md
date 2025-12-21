# Get Performance Test Results

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Gets the results of the performance test for the specified identifier.

**Availability**:
- Retention Messaging 1.3+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

Call this endpoint to retrieve the performance results from a previous test. The API returns a JSON object that contains [`PerformanceTestConfig`](performancetestconfig.md), [`PerformanceTestResponse`](performancetestresponse.md) , and [`Failures`](failures.md) objects that enumerate the parameters the system used to evaluate the server performance, results of the specified test, and information that describes the failures, if any, that the test encountered.

## See Also

- [Initiate Performance Test](initiate-performance-test.md)
  Initiates a performance test


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-performance-test-results)*