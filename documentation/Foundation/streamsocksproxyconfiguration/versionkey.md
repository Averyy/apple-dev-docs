# versionKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Value is either `NSStreamSOCKSProxyVersion4` or `NSStreamSOCKSProxyVersion5`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let versionKey: StreamSOCKSProxyConfiguration
```

```c
extern NSStreamSOCKSProxyConfiguration const NSStreamSOCKSProxyVersionKey;
```

## Discussion

If this key is not present, `NSStreamSOCKSProxyVersion5` is used by default.

## See Also

### Type Properties
- [static let hostKey: StreamSOCKSProxyConfiguration](./hostkey.md)
  Value is an `NSString` object that represents the SOCKS proxy host.
- [static let passwordKey: StreamSOCKSProxyConfiguration](./passwordkey.md)
  Value is an `NSString` object containing the user’s password.
- [static let portKey: StreamSOCKSProxyConfiguration](./portkey.md)
  Value is an `NSNumber` object containing an integer that represents the port on which the proxy listens.
- [static let userKey: StreamSOCKSProxyConfiguration](./userkey.md)
  Value is an `NSString` object containing the user’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamsocksproxyconfiguration/versionkey)*