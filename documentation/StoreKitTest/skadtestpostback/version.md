# version

**Framework**: StoreKit Test  
**Kind**: property

The SKAdNetwork version that the postback uses.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var version: SKAdTestPostbackVersion { get }
```

#### Discussion

For information about the SKAdNetwork versions, See [`SKAdNetwork release notes`](https://developer.apple.com/documentation/StoreKit/skadnetwork-release-notes).

## See Also

- [var transactionIdentifier: String](skadtestpostback/transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](skadtestpostback/postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](skadtestpostback/isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](skadtestpostback/isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/version)*