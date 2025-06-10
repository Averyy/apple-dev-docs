# NSURLAuthenticationMethodHTMLForm

**Framework**: Foundation  
**Kind**: var

Use HTML form authentication for this protection space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSURLAuthenticationMethodHTMLForm: String
```

#### Discussion

The URL loading system never issues authentication challenges based on this authentication method. However, if your app authenticates by submitting a web form (or in some other protocol-neutral way), you can specify this protection space when you persist or look up credentials using the [`URLCredentialStorage`](urlcredentialstorage.md) class.

## See Also

- [let NSURLAuthenticationMethodDefault: String](nsurlauthenticationmethoddefault.md)
  Use the default authentication method for a protocol.
- [let NSURLAuthenticationMethodHTTPBasic: String](nsurlauthenticationmethodhttpbasic.md)
  Use HTTP basic authentication for this protection space.
- [let NSURLAuthenticationMethodHTTPDigest: String](nsurlauthenticationmethodhttpdigest.md)
  Use HTTP digest authentication for this protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodhtmlform)*