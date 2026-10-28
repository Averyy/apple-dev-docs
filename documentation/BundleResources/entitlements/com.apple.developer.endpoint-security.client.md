# com.apple.developer.endpoint-security.client

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The entitlement required to monitor system events for potentially malicious activity.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `com.apple.developer.endpoint-security.client`
- **Type**: boolean

## Discussion

You must request this entitlement from Apple. For information about how to request the entitlement, see [System Extensions and DriverKit](https://developer.apple.com/system-extensions/).

If your app or extension lacks this requirement, [`es_new_client(_:_:)`](../../EndpointSecurity/es_new_client%28_,_%29.md) fails with the result [`ES_NEW_CLIENT_RESULT_ERR_NOT_ENTITLED`](../../EndpointSecurity/es_new_client_result_err_not_entitled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.endpoint-security.client)*