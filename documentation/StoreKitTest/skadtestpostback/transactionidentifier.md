# transactionIdentifier

**Framework**: StoreKit Test  
**Kind**: property

A unique transaction identifier that the system generates.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var transactionIdentifier: String { get }
```

#### Discussion

The system generates this value when you call [`setPostbacks(_:)`](skadtestsession/setpostbacks(_:).md). This value is an empty string otherwise.

Use this value to match the test postback with the response you receive from [`flushPostbacks(responses:)`](skadtestsession/flushpostbacks(responses:).md).

## See Also

- [var version: SKAdTestPostbackVersion](skadtestpostback/version.md)
  The SKAdNetwork version that the postback uses.
- [var postbackSequenceIndex: Int](skadtestpostback/postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](skadtestpostback/isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](skadtestpostback/isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/transactionidentifier)*