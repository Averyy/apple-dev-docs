# trackingAreaCode

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The Tracking Area Code of the private LTE network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var trackingAreaCode: String? { get set }
```

```objc
@property (copy, nullable) NSString * trackingAreaCode;
```

#### Discussion

This property is only applicable for band 48 private LTE networks.

## See Also

### Accessing network properties
- [var mobileCountryCode: String](./mobilecountrycode.md)
  The Mobile Country Code (MCC) of the private LTE network.
- [var mobileNetworkCode: String](./mobilenetworkcode.md)
  The Mobile Network Code (MNC) of the private LTE network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprivateltenetwork/trackingareacode)*