# com.apple.developer.endpoint-security.client

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement required to monitor system events for potentially malicious activity.

**Availability**:
- macOS 10.15+



**Type**: boolean

#### Discussion

You must request this entitlement from Apple. For information about how to request the entitlement, see [`System Extensions and DriverKit`](https://developer.apple.comhttps://developer.apple.com/system-extensions/).

If your app or extension lacks this requirement, [`es_new_client(_:_:)`](https://developer.apple.com/documentation/endpointsecurity/es_new_client(_:_:)) fails with the result [`ES_NEW_CLIENT_RESULT_ERR_NOT_ENTITLED`](https://developer.apple.com/documentation/endpointsecurity/es_new_client_result_err_not_entitled).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.endpoint-security.client)*