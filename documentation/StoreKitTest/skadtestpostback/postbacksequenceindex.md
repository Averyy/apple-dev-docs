# postbackSequenceIndex

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The position of this postback among all postbacks for an ad impression.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var postbackSequenceIndex: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger postbackSequenceIndex;
```

## Discussion

For more information about receiving time-delayed postbacks for an ad impression, see [Receiving postbacks in multiple conversion windows](../../StoreKit/receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

### Getting general information
- [var version: SKAdTestPostbackVersion](./version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](./transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var isRegistered: Bool](./isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](./isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/postbacksequenceindex)*