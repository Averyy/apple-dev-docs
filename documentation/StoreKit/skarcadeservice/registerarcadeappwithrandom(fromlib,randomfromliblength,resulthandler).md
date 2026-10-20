# registerArcadeAppWithRandom(fromLib:randomFromLibLength:resultHandler:)

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
class func registerArcadeAppWithRandom(fromLib randomFromLib: Data, randomFromLibLength: UInt32, resultHandler: @escaping (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)
```

```objc
+ (void) registerArcadeAppWithRandomFromLib:(NSData *) randomFromLib randomFromLibLength:(uint32_t) randomFromLibLength resultHandler:(void (^)(NSData *randomFromFP, uint32_t randomFromFPLength, NSData *cmacOfAppPID, uint32_t cmacOfAppPIDLength, NSError *error)) resultHandler;
```

## See Also

### Type Methods
- [class func arcadeSubscriptionStatus(withNonce: UInt64, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](./arcadesubscriptionstatus%28withnonce,resulthandler%29.md)
- [class func repairArcadeApp()](./repairarcadeapp%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skarcadeservice/registerarcadeappwithrandom(fromlib:randomfromliblength:resulthandler:))*