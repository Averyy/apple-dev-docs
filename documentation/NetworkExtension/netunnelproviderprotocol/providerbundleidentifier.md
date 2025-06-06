# providerBundleIdentifier

**Framework**: Network Extension  
**Kind**: property

A string identifying the specific Tunnel Provider extension that should be used with this configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var providerBundleIdentifier: String? { get set }
```

#### Discussion

A single app may contain multiple Tunnel Provider extensions. This property is used to specify which Tunnel Provider extension should be used with this configuration.

## See Also

- [var providerConfiguration: [String : Any]?](netunnelproviderprotocol/providerconfiguration.md)
  A dictionary containing keys and values defined by the Tunnel Provider developer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/providerbundleidentifier)*