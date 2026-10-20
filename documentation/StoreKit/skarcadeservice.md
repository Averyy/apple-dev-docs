# SKArcadeService

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SKArcadeService : NSObject
```

## Topics

### Type Methods
- [class func arcadeSubscriptionStatus(withNonce: UInt64, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](./skarcadeservice/arcadesubscriptionstatus%28withnonce,resulthandler%29.md)
- [class func registerArcadeAppWithRandom(fromLib: Data, randomFromLibLength: UInt32, resultHandler: (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)](./skarcadeservice/registerarcadeappwithrandom%28fromlib,randomfromliblength,resulthandler%29.md)
- [class func repairArcadeApp()](./skarcadeservice/repairarcadeapp%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loading the setup view
- [Offering Apple Music Subscription in Your App](./offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [struct SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](./skcloudservicesetupviewcontroller/load%28options,completionhandler%29.md)
  Loads the cloud service setup view with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skarcadeservice)*