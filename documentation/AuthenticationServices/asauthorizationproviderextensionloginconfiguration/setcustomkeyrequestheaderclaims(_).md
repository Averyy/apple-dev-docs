# setCustomKeyRequestHeaderClaims(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func setCustomKeyRequestHeaderClaims(_ claims: [String : Any]) throws
```

```objc
- (BOOL) setCustomKeyRequestHeaderClaims:(NSDictionary<NSString *,id> *) claims returningError:(NSError **) error;
```

## Mentions

- [Supporting key requests and key exchange requests](../supporting-key-requests-and-key-exchange-requests.md)

## See Also

### Instance Methods
- [func setCustomKeyExchangeRequestBodyClaims([String : Any]) throws](./setcustomkeyexchangerequestbodyclaims%28_%29.md)
- [func setCustomKeyExchangeRequestHeaderClaims([String : Any]) throws](./setcustomkeyexchangerequestheaderclaims%28_%29.md)
- [func setCustomKeyRequestBodyClaims([String : Any]) throws](./setcustomkeyrequestbodyclaims%28_%29.md)
- [func setCustomRefreshRequestBodyClaims([String : Any]) throws](./setcustomrefreshrequestbodyclaims%28_%29.md)
- [func setCustomRefreshRequestHeaderClaims([String : Any]) throws](./setcustomrefreshrequestheaderclaims%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/setcustomkeyrequestheaderclaims(_:))*