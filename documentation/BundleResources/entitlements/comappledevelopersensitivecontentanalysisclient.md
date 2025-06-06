# com.apple.developer.sensitivecontentanalysis.client

**Framework**: Bundle Resources  
**Kind**: typealias

A code-signing entitlement that enables an app to detect nudity in images and video.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

#### Discussion

The [`SensitiveContentAnalysis`](https://developer.apple.com/documentation/SensitiveContentAnalysis) framework fails to return positive results for apps that lack this entitlement in its code signature.

You can add this entitlement to your app by enabling the Sensitive Content Analysis capability in Xcode. For more information, see [`Detecting nudity in media and providing intervention options`](https://developer.apple.com/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sensitivecontentanalysis.client)*