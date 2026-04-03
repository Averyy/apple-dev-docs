# Initiate Performance Test

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Initiates a performance test of your Get Retention Message endpoint in the sandbox environment.

**Availability**:
- Retention Messaging API 1.3+

## Mentions

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
- [Identifying rate limits](identifying-rate-limits.md)
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

Call this endpoint after you configure your `Get Retention Message` endpoint for the sandbox environment to test your server’s performance. The service returns a response that includes a [`PerformanceTestConfig`](performancetestconfig.md) object that describes the testing parameters and a `requestId` you can use to request test results.

> **Note**: The performance test runs only in the sandbox environment. Use original transaction identifiers of transactions you initiate in the sandbox environment. For more information, see [`PerformanceTestRequest`](performancetestrequest.md).

To pass the performance test, your server must respond to requests within approximately 700 ms in the sandbox environment. For a more precise response-time value, run the test and check the [`PerformanceTestConfig`](performancetestconfig.md) in the [`PerformanceTestResponse`](performancetestresponse.md). See the `responseTimeThreshold` value for the required response time in the sandbox environment.

Your server needs to pass the performance test before you can configure a real-time URL for your `Get Retention Message` endpoint in the production environment. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

## Endpoint

`POST https://api.storekit-sandbox.itunes.apple.com/inApps/v1/messaging/performanceTest`

## Request Body

The request body which specifies a transaction identifier of an In-App Purchase to use for this test.

## See Also

- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.
- [object PerformanceTestRequest](performancetestrequest.md)
  The request object you provide for a performance test that contains an original transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/initiate-performance-test)*