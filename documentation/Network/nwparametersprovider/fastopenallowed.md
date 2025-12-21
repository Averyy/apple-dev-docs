# fastOpenAllowed(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Allow fast open to be used on a connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func fastOpenAllowed(_ allowed: Bool) -> Self
```

#### Discussion

Use fast open for an outbound connection, which may be done at any protocol level. Use of fast open requires that the caller send idempotent data on the connection before the connection may move into the ready state.

> ⚠️ **Warning**: This may have security implications for application data. In particular, TLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.

As a side effect, this may implicitly enable fast open or early data for protocols in the stack, even if they did not have fast open explicitly enabled on them (such as the option to enable TCP Fast Open).

## Parameters

- `allowed`: True if fast open should be used, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/fastopenallowed(_:))*