# List all beta app clip invocations for a build bundle

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

- [Read the app clip domain cache status information for a build bundle](get-v1-buildbundles-_id_-appclipdomaincachestatus.md)
  Get the cache status of the domain you associate with your App Clip for a specific build bundle.
- [Read app clip domain debug status information for a build bundle](get-v1-buildbundles-_id_-appclipdomaindebugstatus.md)
  Get the debug status of the domain you associate with your App Clip for a specific build bundle.
- [List all file sizes for a build bundle](get-v1-buildbundles-_id_-buildbundlefilesizes.md)
  Get all file sizes for a specific build bundle.
- [Get the App Clip domain cache status ID for a build bundle](get-v1-buildbundles-_id_-relationships-appclipdomaincachestatus.md)
- [Get the App Clip domain debug status ID for a build bundle](get-v1-buildbundles-_id_-relationships-appclipdomaindebugstatus.md)
- [List beta App Clip invocation IDs for a build bundle](get-v1-buildbundles-_id_-relationships-betaappclipinvocations.md)
- [List file size IDs for a build bundle](get-v1-buildbundles-_id_-relationships-buildbundlefilesizes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbundles-_id_-betaappclipinvocations)*