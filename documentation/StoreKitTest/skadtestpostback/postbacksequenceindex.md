# postbackSequenceIndex

**Framework**: StoreKit Test  
**Kind**: property

The position of this postback among all postbacks for an ad impression.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var postbackSequenceIndex: Int { get }
```

#### Discussion

For more information about receiving time-delayed postbacks for an ad impression, see [`Receiving postbacks in multiple conversion windows`](https://developer.apple.com/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [var version: SKAdTestPostbackVersion](skadtestpostback/version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](skadtestpostback/transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var isRegistered: Bool](skadtestpostback/isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](skadtestpostback/isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/postbacksequenceindex)*