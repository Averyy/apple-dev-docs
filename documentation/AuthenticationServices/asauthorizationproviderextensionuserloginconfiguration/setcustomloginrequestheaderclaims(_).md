# setCustomLoginRequestHeaderClaims(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func setCustomLoginRequestHeaderClaims(_ claims: [String : Any]) throws
```

```objc
- (BOOL) setCustomLoginRequestHeaderClaims:(NSDictionary<NSString *,id> *) claims returningError:(NSError **) error;
```

## See Also

### Instance Methods
- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](./setcustomassertionrequestbodyclaims%28_%29.md)
- [func setCustomAssertionRequestHeaderClaims([String : Any]) throws](./setcustomassertionrequestheaderclaims%28_%29.md)
- [func setCustomLoginRequestBodyClaims([String : Any]) throws](./setcustomloginrequestbodyclaims%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionuserloginconfiguration/setcustomloginrequestheaderclaims(_:))*