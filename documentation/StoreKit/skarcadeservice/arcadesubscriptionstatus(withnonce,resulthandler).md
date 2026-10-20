# arcadeSubscriptionStatus(withNonce:resultHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func arcadeSubscriptionStatus(withNonce nonce: UInt64, resultHandler: @escaping (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)
```

```objc
+ (void) arcadeSubscriptionStatusWithNonce:(uint64_t) nonce resultHandler:(void (^)(NSData *subscriptionStatus, uint32_t subscriptionStatusLength, NSData *cmacOfNonce, uint32_t cmacOfNonceLength, NSError *error)) resultHandler;
```

## See Also

### Type Methods
- [class func registerArcadeAppWithRandom(fromLib: Data, randomFromLibLength: UInt32, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](./registerarcadeappwithrandom%28fromlib,randomfromliblength,resulthandler%29.md)
- [class func repairArcadeApp()](./repairarcadeapp%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skarcadeservice/arcadesubscriptionstatus(withnonce:resulthandler:))*