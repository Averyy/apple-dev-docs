# isSupported

**Framework**: ARKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the current runtime environment supports a particular provider type.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static var isSupported: Bool { get }
```

#### Discussion

For example, data providers are not supported in Simulator.

## See Also

- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](dataprovider/requiredauthorizations.md)
  The kinds of authorization you need to use a particular data provider type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/dataprovider/issupported)*