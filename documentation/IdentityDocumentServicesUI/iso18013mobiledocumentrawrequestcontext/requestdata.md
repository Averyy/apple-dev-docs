# requestData

**Framework**: IdentityDocumentServicesUI  
**Kind**: property  
**Role**: Instance Property

Incoming request data that uses a JSON format the ISO 18013 request profile defines.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
let requestData: Data
```

## Discussion

Decode the raw request data to determine which documents and elements the relying party requests before you present authorization UI.

## See Also

### Reading the request
- [let requestingWebsiteOrigin: URL?](./requestingwebsiteorigin.md)
  The origin of the requesting website, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrawrequestcontext/requestdata)*