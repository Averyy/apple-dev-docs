# supportedChargingConnectors

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The charging connectors that the electric vehicle supports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var supportedChargingConnectors: [INCar.ChargingConnectorType] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * supportedChargingConnectors;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<NSString *> * supportedChargingConnectors;
```

## See Also

### Getting the Car’s Supported Charging Connectors
- [struct ChargingConnectorType](./chargingconnectortype.md)
  Constants that describe the available charging connector types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/supportedchargingconnectors)*