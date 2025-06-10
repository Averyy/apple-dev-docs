# registerArcadeAppWithRandom(fromLib:randomFromLibLength:resultHandler:)

**Framework**: StoreKit  
**Kind**: method

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

## See Also

- [class func arcadeSubscriptionStatus(withNonce: UInt64, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](skarcadeservice/arcadesubscriptionstatus(withnonce:resulthandler:).md)
- [class func repairArcadeApp()](skarcadeservice/repairarcadeapp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skarcadeservice/registerarcadeappwithrandom(fromlib:randomfromliblength:resulthandler:))*