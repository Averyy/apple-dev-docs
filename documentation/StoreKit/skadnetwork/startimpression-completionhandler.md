# startImpression(_:completionHandler:)

**Framework**: Storekit  
**Kind**: method

Indicates that your app is presenting a view-through ad to the user.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
class func startImpression(_ impression: SKAdImpression) async throws
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
- [Signing and providing ads](signing-and-providing-ads.md)
- [SKAdNetwork 2.2 release notes](skadnetwork-2-2-release-notes.md)

#### Discussion

Call this method when you start presenting the view-through ad to the user. If you call [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md) more than once for the same advertised app before calling [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md), the latest impression overwrites the earlier impression.

Call [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md) when the impression ends and is no longer visible to the user.

> **Note**:  To ensure that SKAdNetwork records the impression, call [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md) after the impression ends, regardless of whether [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md) returns an error in the completion handler.

## Parameters

- `impression`: An instance of   with the properties set for the view-through ad that you’re presenting.
- `completion`: The callback handler you provide to handle any tasks relevant to the start of the ad impression.

## See Also

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
  Initiate install validation by displaying a view-through ad with signed parameters.
- [class SKAdImpression](skadimpression.md)
  A class that defines an ad impression for a view-through ad.
- [class func endImpression(SKAdImpression, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/endimpression(_:completionhandler:).md)
  Indicates that your app is no longer presenting a view-through ad to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/startimpression(_:completionhandler:))*