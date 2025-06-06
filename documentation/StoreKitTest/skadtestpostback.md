# SKAdTestPostback

**Framework**: StoreKit Test  
**Kind**: class

A test postback that contains ad conversion information in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
class SKAdTestPostback
```

#### Overview

Use this class to create test postbacks to use for unit testing.

In the production environment, the system creates a postback after a user installs an advertised app. The advertised app is responsible for registering the installation and may update the conversion value. The system sends the postback after a timer expires.

In the testing environment, you can mimic a postback by creating it directly. You control the property values within the postback. Use it to test your app’s ability to register the app installation and update conversion values, and to test your server’s ability to receive postbacks.

## Topics

### Creating test postbacks
- [init?(version: SKAdTestPostbackVersion, adNetworkIdentifier: String, sourceIdentifier: String, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, sourceDomain: String?, fidelityType: Int, isRedownload: Bool, didWin: Bool, postbackURL: String)](skadtestpostback/init(version:adnetworkidentifier:sourceidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:sourcedomain:fidelitytype:isredownload:didwin:postbackurl:).md)
  Creates a test postback for a web ad or an in-app ad.
- [class func winningPostbacks(withVersion: SKAdTestPostbackVersion, adNetworkIdentifier: String, sourceIdentifier: String, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, sourceDomain: String?, fidelityType: Int, isRedownload: Bool, postbackURL: String) -> [SKAdTestPostback]?](skadtestpostback/winningpostbacks(withversion:adnetworkidentifier:sourceidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:sourcedomain:fidelitytype:isredownload:postbackurl:).md)
  Creates a sequence of test postbacks for an in-app or web ad impression.
- [init?(version: SKAdTestPostbackVersion, adNetworkIdentifier: String, adCampaignIdentifier: Int, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, conversionValue: Int, fidelityType: Int, isRedownload: Bool, didWin: Bool, postbackURL: String)](skadtestpostback/init(version:adnetworkidentifier:adcampaignidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:conversionvalue:fidelitytype:isredownload:didwin:postbackurl:).md)
  Creates a test postback for an in-app ad.
### Getting the Postback Destination
- [var postbackURL: String](skadtestpostback/postbackurl.md)
  A URL on your server where the testing environment sends test postbacks.
### Getting general information
- [var version: SKAdTestPostbackVersion](skadtestpostback/version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](skadtestpostback/transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](skadtestpostback/postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](skadtestpostback/isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](skadtestpostback/isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.
### Getting advertisement information
- [var adNetworkIdentifier: String](skadtestpostback/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](skadtestpostback/appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](skadtestpostback/sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceDomain: String?](skadtestpostback/sourcedomain.md)
  The source of a web ad.
- [var sourceIdentifier: String?](skadtestpostback/sourceidentifier.md)
  A string that identifies an ad campaign.
### Getting conversion information
- [var fidelityType: Int](skadtestpostback/fidelitytype.md)
  An integer that indicates the type of ad impression, StoreKit-rendered or view-through.
- [var fineConversionValue: Int](skadtestpostback/fineconversionvalue.md)
  The specific conversion value of an ad postback.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](skadtestpostback/coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.
- [var didWin: Bool](skadtestpostback/didwin.md)
  A Boolean value that indicates whether the postback won the attribution.
### Getting information in earlier versions
- [var adCampaignIdentifier: Int](skadtestpostback/adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.
- [var conversionValue: Int](skadtestpostback/conversionvalue.md)
  An unsigned 6-bit value that the app or ad network controls.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- [class SKAdTestSession](skadtestsession.md)
  The class you use to test ad impressions and postbacks in Xcode.
- [class SKAdTestPostbackResponse](skadtestpostbackresponse.md)
  The status and error information for a postback that the system sends in the testing environment.
- [struct SKAdTestPostbackVersion](skadtestpostbackversion.md)
  A constant that indicates the postback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback)*