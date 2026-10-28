# configuration

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The configuration of the provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var configuration: CXProviderConfiguration { get set }
```

```objc
@property (nonatomic, copy, readwrite) CXProviderConfiguration * configuration;
```

## Discussion

This property returns a copy of the provider configuration. To change the configuration of the provider, you must set this property to a  new [`CXProviderConfiguration`](../cxproviderconfiguration.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/configuration)*