# AppImpression

**Framework**: AdAttributionKit  
**Kind**: struct

A structure that represents an attributable impression you generate in response to a person’s interaction with an ad in an app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
struct AppImpression
```

## Mentions

- [Generating JWS impressions](generating-jws-impressions.md)
- [Presenting ads in your app](presenting-ads-in-your-app.md)

#### Discussion

To record a view-through impression, call [`beginView()`](appimpression/beginview().md) when the ad content corresponding to the impression becomes visible, and [`endView()`](appimpression/endview().md) when the ad content disappears. The advertisement needs to be visible for at least two seconds for AdAttributionKit to record a view through impression; otherwise, the framework throws an error.

> ❗ **Important**:  Regenerate an `AppImpression` for each ad you show. Don’t reuse `AppImpression` structures across multiple ads.

To support click-through attribution, place a [`UIEventAttributionView`](https://developer.apple.com/documentation/UIKit/UIEventAttributionView) over the ad content and call  either [`handleTap(reengagementURL:)`](appimpression/handletap(reengagementurl:).md) or [`handleTap()`](appimpression/handletap().md) after a person taps the ad content. The framework then validates that a person taps a `UIEventAttributionView` before recording the impression, and throws an error if it can’t validate that a tap occurred in a `UIEventAttributionView`.

After the framework validates the tap, it records the impression and then attempts to launch one of the user’s installed marketplaces to show the product page for the advertised app. The system uses the advertised item ID from the JSON Web Signature (JWS) string you provide to initialize the `AppImpression`, in addition to the user’s preferred marketplaces, to help determine which marketplace the framework needs to launch. If the app is already installed, the framework launches into the app’s Home Screen instead.

In iOS 18 and later, `AppImpression` supports reengagement for click-through interactions when the advertised app is already installed on the device. The system can deep-link into the advertised app when using [`handleTap(reengagementURL:)`](appimpression/handletap(reengagementurl:).md). Click-through impressions can also qualify for reengagement postbacks by opting in for reengagement in the impression JWS. For more information about opting in for re-engagement, see [`Generating JWS impressions`](generating-jws-impressions.md).

## Topics

### Creating an ad impression
- [init(compactJWS: String) async throws](appimpression/init(compactjws:).md)
  Creates a new app impression with the provided compact JSON Web Signature (JWS).
### Displaying view-through ads
- [func beginView() async throws](appimpression/beginview.md)
  Begins recording a view-through impression when ad content corresponding to the impression becomes visible.
- [func endView() async throws](appimpression/endview.md)
  Ends the view-through impression when the ad content corresponding to the impression disappears.
- [func handleView() async throws](appimpression/handleview.md)
  Handles a view through ad impression.
### Processing interactions with click-through ads
- [func handleTap() async throws](appimpression/handletap.md)
  Processes click-through interactions on your custom rendered ad content.
- [func handleTap(reengagementURL: URL) async throws](appimpression/handletap(reengagementurl:).md)
  Processes click-through interactions on your custom rendered ad content, and delivers a URL to the advertised app if it’s installed.
### Accessing ad impression properties
- [var adNetworkID: String](appimpression/adnetworkid.md)
  The advertising network ID.
- [var advertisedItemID: UInt64](appimpression/advertiseditemid.md)
  The advertised item’s ID.
- [var compactJWSRepresentation: String](appimpression/compactjwsrepresentation.md)
  A string that presents the compact representation of the impression’s JSON Web Signature (JWS).
- [var eligibleForReengagement: Bool](appimpression/eligibleforreengagement.md)
  A Boolean value that indicates whether this impression is eligible for reengagement.
- [var id: UUID](appimpression/id.md)
  The impression’s unique ID.
- [var keyID: String](appimpression/keyid.md)
  The JSON Web Signature (JWS) key ID.
- [var publisherItemID: UInt64](appimpression/publisheritemid.md)
  The publisher app’s item ID.
- [var sourceID: Int](appimpression/sourceid.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var timestamp: Date](appimpression/timestamp.md)
  The impression’s timestamp, in milliseconds since 1970.
### Checking device support
- [static var isSupported: Bool](appimpression/issupported.md)
  A Boolean value that indicates whether the framework supports app impressions on a person’s device.
### Comparing and hashing ad impressions
- [static func == (AppImpression, AppImpression) -> Bool](appimpression/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
- [func hash(into: inout Hasher)](appimpression/hash(into:).md)
  A function that hashes the essential components of the value by passing them into the hasher.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression)*