# isRedownload

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the user redownloaded and reinstalled the app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var isRedownload: Bool { get }
```

#### Discussion

In the production environment, this value is `true` when the user redownloaded and reinstalled the app. In the testing environment, you set the value of this property when you create the test postback.

## See Also

- [var version: SKAdTestPostbackVersion](skadtestpostback/version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](skadtestpostback/transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](skadtestpostback/postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](skadtestpostback/isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/isredownload)*