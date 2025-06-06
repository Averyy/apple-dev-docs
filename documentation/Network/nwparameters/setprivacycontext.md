# setPrivacyContext(_:)

**Framework**: Network  
**Kind**: method

Associates a privacy context with any connections or listeners that use the parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
final func setPrivacyContext(_ privacyContext: NWParameters.PrivacyContext)
```

#### Discussion

The privacy context allows using separate caches for different sets of connections, as well as restricting how connection-specific information is logged and shared on the network.

## See Also

- [NWParameters.PrivacyContext](nwparameters/privacycontext.md)
  An object that defines the privacy requirements for a set of connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/setprivacycontext(_:))*