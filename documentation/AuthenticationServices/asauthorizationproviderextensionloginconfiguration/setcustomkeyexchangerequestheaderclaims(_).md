# setCustomKeyExchangeRequestHeaderClaims(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func setCustomKeyExchangeRequestHeaderClaims(_ claims: [String : Any]) throws
```

```objc
- (BOOL) setCustomKeyExchangeRequestHeaderClaims:(NSDictionary<NSString *,id> *) claims returningError:(NSError **) error;
```

## See Also

### Instance Methods
- [func setCustomKeyExchangeRequestBodyClaims([String : Any]) throws](./setcustomkeyexchangerequestbodyclaims%28_%29.md)
- [func setCustomKeyRequestBodyClaims([String : Any]) throws](./setcustomkeyrequestbodyclaims%28_%29.md)
- [func setCustomKeyRequestHeaderClaims([String : Any]) throws](./setcustomkeyrequestheaderclaims%28_%29.md)
- [func setCustomRefreshRequestBodyClaims([String : Any]) throws](./setcustomrefreshrequestbodyclaims%28_%29.md)
- [func setCustomRefreshRequestHeaderClaims([String : Any]) throws](./setcustomrefreshrequestheaderclaims%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/setcustomkeyexchangerequestheaderclaims(_:))*