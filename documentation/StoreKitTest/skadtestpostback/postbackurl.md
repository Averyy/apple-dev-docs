# postbackURL

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A URL on your server where the testing environment sends test postbacks.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var postbackURL: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * postbackURL;
```

## Discussion

The testing environment sends the test postback to the [`postbackURL`](./postbackurl.md) when you call [`flushPostbacks(responses:)`](../skadtestsession/flushpostbacks%28responses%29.md).

> **Note**:  Ensure that your test server is running and accepting connections before calling [`flushPostbacks(responses:)`](../skadtestsession/flushpostbacks%28responses%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/postbackurl)*