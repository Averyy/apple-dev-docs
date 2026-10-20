# webServiceURL

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The URL for the web service.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var webServiceURL: URL? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * webServiceURL;
```

#### Discussion

The web service is for updating passes. For information about the web service protocol, see [PassKit Web Service Reference](https://developer.apple.com/library/archive/documentation/PassKit/Reference/PassKit_WebService/WebService.html#//apple_ref/doc/uid/TP40011988).

## See Also

### Getting the web service information
- [var authenticationToken: String?](./authenticationtoken.md)
  The token for authenticating update requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/webserviceurl)*