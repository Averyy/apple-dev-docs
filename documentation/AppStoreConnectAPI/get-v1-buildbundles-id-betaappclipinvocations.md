# List All Beta App Clip Invocations for a Build Bundle

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all App Clip invocations you configure for testing for a specific build bundle.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBundles/{id}/betaAppClipInvocations`

## Parameters

- `fields[betaAppClipInvocationLocalizations]` ([string]): Additional fields to include for each Beta App Clip Invocation resource returned by the response.
- `fields[betaAppClipInvocations]` ([string]): Additional fields to include for each Beta App Clip Invocation resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Beta App Clip Invocations resources to return.
- `limit[betaAppClipInvocationLocalizations]` (integer): The number of included Beta App Clip Invocations resources to return if the beta App Clip invocation localizations relationship is included.

## See Also

- [Read the App Clip Domain Cache Status Information for a Build Bundle](get-v1-buildbundles-_id_-appclipdomaincachestatus.md)
  Get the cache status of the domain you associate with your App Clip for a specific build bundle.
- [Read App Clip Domain Debug Status Information for a Build Bundle](get-v1-buildbundles-_id_-appclipdomaindebugstatus.md)
  Get the debug status of the domain you associate with your App Clip for a specific build bundle.
- [List All File Sizes for a Build Bundle](get-v1-buildbundles-_id_-buildbundlefilesizes.md)
  Get all file sizes for a specific build bundle.
- [GET /v1/buildBundles/{id}/relationships/appClipDomainCacheStatus](get-v1-buildbundles-_id_-relationships-appclipdomaincachestatus.md)
- [GET /v1/buildBundles/{id}/relationships/appClipDomainDebugStatus](get-v1-buildbundles-_id_-relationships-appclipdomaindebugstatus.md)
- [GET /v1/buildBundles/{id}/relationships/betaAppClipInvocations](get-v1-buildbundles-_id_-relationships-betaappclipinvocations.md)
- [GET /v1/buildBundles/{id}/relationships/buildBundleFileSizes](get-v1-buildbundles-_id_-relationships-buildbundlefilesizes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbundles-_id_-betaappclipinvocations)*