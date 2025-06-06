# isRegistered

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the postback is registered in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var isRegistered: Bool { get }
```

#### Discussion

To register a postback, call [`updatePostbackConversionValue(_:completionHandler:)`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)), or [`registerAppForAdNetworkAttribution()`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()).

## See Also

- [var version: SKAdTestPostbackVersion](skadtestpostback/version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](skadtestpostback/transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](skadtestpostback/postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRedownload: Bool](skadtestpostback/isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/isregistered)*