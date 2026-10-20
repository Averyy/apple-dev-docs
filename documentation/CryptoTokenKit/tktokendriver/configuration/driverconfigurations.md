# driverConfigurations

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Type Property

A dictionary of token class configurations which the class identifier of the token driver keys.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class var driverConfigurations: [TKTokenDriver.ClassID : TKTokenDriver.Configuration] { get }
```

```objc
@property (class, nonatomic, readonly) NSDictionary<NSString *,TKTokenDriverConfiguration *> * driverConfigurations;
```

#### Discussion

If the app hosting the token extension calls this method, it returns a list of configurations for hosted token extensions. Otherwise, this method returns an empty array.

## See Also

### Reporting Configuration Information
- [var classID: TKTokenDriver.ClassID](./classid.md)
  The class identifier of the token driver.
- [var tokenConfigurations: [TKToken.InstanceID : TKToken.Configuration]](./tokenconfigurations.md)
  A dictionary of all currently configured tokens for this token class, which the token instance identifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/configuration/driverconfigurations)*