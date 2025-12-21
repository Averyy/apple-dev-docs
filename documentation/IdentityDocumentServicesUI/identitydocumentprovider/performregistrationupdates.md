# performRegistrationUpdates()

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Required**: Yes

A function that allows the current app to perform updates to document registrations to ensure consistency with documents stored in the app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
func performRegistrationUpdates() async
```

#### Discussion

The system calls this function periodically, including when the person enables the current app to provide documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentprovider/performregistrationupdates())*