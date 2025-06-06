# SKArcadeService

**Framework**: StoreKit  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SKArcadeService
```

## Topics

### Type Methods
- [class func arcadeSubscriptionStatus(withNonce: UInt64, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](skarcadeservice/arcadesubscriptionstatus(withnonce:resulthandler:).md)
- [class func registerArcadeAppWithRandom(fromLib: Data, randomFromLibLength: UInt32, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](skarcadeservice/registerarcadeappwithrandom(fromlib:randomfromliblength:resulthandler:).md)
- [class func repairArcadeApp()](skarcadeservice/repairarcadeapp.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [struct SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](skcloudservicesetupviewcontroller/load(options:completionhandler:).md)
  Loads the cloud service setup view with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skarcadeservice)*