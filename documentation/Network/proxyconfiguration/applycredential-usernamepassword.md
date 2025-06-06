# applyCredential(username:password:)

**Framework**: Network  
**Kind**: method

Sets a username and password to use as authentication for a proxy configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func applyCredential(username: String, password: String)
```

## Parameters

- `username`: A proxy authentication username.
- `password`: A proxy authentication password.

## See Also

- [var allowFailover: Bool](proxyconfiguration/allowfailover.md)
  A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/applycredential(username:password:))*