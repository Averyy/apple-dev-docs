# requestingWebsiteOrigin

**Framework**: IdentityDocumentServicesUI  
**Kind**: property  
**Role**: Instance Property

The origin of the requesting website, if present.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
let requestingWebsiteOrigin: URL?
```

## Discussion

Show this value to the person using your app so they can identify who’s requesting their data. The value is `nil` when the request doesn’t come from a website.

## See Also

### Reading the request
- [let requestData: Data](./requestdata.md)
  Incoming request data that uses a JSON format the ISO 18013 request profile defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrawrequestcontext/requestingwebsiteorigin)*