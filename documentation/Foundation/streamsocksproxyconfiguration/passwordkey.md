# passwordKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Value is an `NSString` object containing the user’s password.

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
static let passwordKey: StreamSOCKSProxyConfiguration
```

```c
extern NSStreamSOCKSProxyConfiguration const NSStreamSOCKSProxyPasswordKey;
```

## See Also

### Type Properties
- [static let hostKey: StreamSOCKSProxyConfiguration](./hostkey.md)
  Value is an `NSString` object that represents the SOCKS proxy host.
- [static let portKey: StreamSOCKSProxyConfiguration](./portkey.md)
  Value is an `NSNumber` object containing an integer that represents the port on which the proxy listens.
- [static let userKey: StreamSOCKSProxyConfiguration](./userkey.md)
  Value is an `NSString` object containing the user’s name.
- [static let versionKey: StreamSOCKSProxyConfiguration](./versionkey.md)
  Value is either `NSStreamSOCKSProxyVersion4` or `NSStreamSOCKSProxyVersion5`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamsocksproxyconfiguration/passwordkey)*