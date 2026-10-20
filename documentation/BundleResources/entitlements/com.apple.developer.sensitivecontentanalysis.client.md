# com.apple.developer.sensitivecontentanalysis.client

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A code-signing entitlement that enables an app to detect nudity in images and video.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Details

- **Name**: `com.apple.developer.sensitivecontentanalysis.client`
- **Type**: array of string 

## Possible Values

- `analysis`

#### Discussion

The [Sensitive Content Analysis](../../SensitiveContentAnalysis/SensitiveContentAnalysis.md) framework fails to return positive results for apps that lack this entitlement in its code signature.

You can add this entitlement to your app by enabling the Sensitive Content Analysis capability in Xcode. For more information, see [Detecting sensitive content in media and providing intervention options](../../SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sensitivecontentanalysis.client)*