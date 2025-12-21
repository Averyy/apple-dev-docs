# isEnabled

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether the configuration is enabled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final var isEnabled: Bool { get set }
```

#### Discussion

The system starts the providers only when this property is `true`.

## See Also

- [var evaluationProviderBundleIdentifier: String?](nehotspotmanager/evaluationproviderbundleidentifier.md)
  The bundle identifier of the hotspot evaluation provider.
- [var authenticationProviderBundleIdentifier: String?](nehotspotmanager/authenticationproviderbundleidentifier.md)
  The bundle identifier of the hotspot authentication provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/isenabled)*