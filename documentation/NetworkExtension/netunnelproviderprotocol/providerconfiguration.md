# providerConfiguration

**Framework**: Network Extension  
**Kind**: property

A dictionary containing keys and values defined by the Tunnel Provider developer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var providerConfiguration: [String : Any]? { get set }
```

#### Discussion

All of the keys and values in this dictionary must conform to the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) and [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocols.

## See Also

- [var providerBundleIdentifier: String?](netunnelproviderprotocol/providerbundleidentifier.md)
  A string identifying the specific Tunnel Provider extension that should be used with this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/providerconfiguration)*