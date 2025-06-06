# kCFStreamPropertySOCKSVersion

**Framework**: Core Foundation  
**Kind**: var

Constant for the SOCKS version key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCFStreamPropertySOCKSVersion: CFString
```

#### Discussion

Its value must be `kCFStreamSocketSOCKSVersion4` or `kCFStreamSocketSOCKSVersion5` to set SOCKS4 or SOCKS5, respectively. If this key is not present, SOCKS5 is used by default.

## See Also

- [let kCFStreamPropertySOCKSProxyHost: CFString](kcfstreampropertysocksproxyhost.md)
  Constant for the SOCKS proxy host key.
- [let kCFStreamPropertySOCKSProxyPort: CFString](kcfstreampropertysocksproxyport.md)
  Constant for the SOCKS proxy host port key.
- [let kCFStreamSocketSOCKSVersion4: CFString](kcfstreamsocketsocksversion4.md)
  Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [let kCFStreamSocketSOCKSVersion5: CFString](kcfstreamsocketsocksversion5.md)
  Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [let kCFStreamPropertySOCKSUser: CFString](kcfstreampropertysocksuser.md)
  Constant for the key required to set a user name.
- [let kCFStreamPropertySOCKSPassword: CFString](kcfstreampropertysockspassword.md)
  Constant for the key required to set a user’s password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksversion)*