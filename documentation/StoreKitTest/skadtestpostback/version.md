# version

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The SKAdNetwork version that the postback uses.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var version: SKAdTestPostbackVersion { get }
```

```objc
@property (nonatomic, strong, readonly) SKAdTestPostbackVersion version;
```

#### Discussion

For information about the SKAdNetwork versions, See [SKAdNetwork release notes](../../StoreKit/skadnetwork-release-notes.md).

## See Also

### Getting general information
- [var transactionIdentifier: String](./transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](./postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](./isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](./isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/version)*