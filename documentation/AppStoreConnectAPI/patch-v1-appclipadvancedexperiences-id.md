# Modify and delete an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update and delete an existing advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the advanced App Clip experience resource ID from the [`List all advanced app clip experiences for an app clip`](get-v1-appclips-_id_-appclipadvancedexperiences.md) response.

## Request Body

The request body you use to update an advanced App Clip experience.

## See Also

- [Read advanced app clip experience information](get-v1-appclipadvancedexperiences-_id_.md)
  Get information about a specific advanced App Clip experience.
- [Create an advanced app clip experience](post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipadvancedexperiences-_id_)*