# transactionIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A unique transaction identifier that the system generates.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var transactionIdentifier: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * transactionIdentifier;
```

## Discussion

The system generates this value when you call [`setPostbacks(_:)`](../skadtestsession/setpostbacks%28_%29.md). This value is an empty string otherwise.

Use this value to match the test postback with the response you receive from [`flushPostbacks(responses:)`](../skadtestsession/flushpostbacks%28responses%29.md).

## See Also

### Getting general information
- [var version: SKAdTestPostbackVersion](./version.md)
  The SKAdNetwork version that the postback uses.
- [var postbackSequenceIndex: Int](./postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRegistered: Bool](./isregistered.md)
  A Boolean value that indicates whether the postback is registered in the testing environment.
- [var isRedownload: Bool](./isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/transactionidentifier)*