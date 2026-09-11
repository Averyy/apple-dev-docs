# userIdentity()

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

Returns the information for the current contact.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func userIdentity() -> ResolvedContact
```

#### Return Value

A resolved contact structure with information your app manages. Fill this structure with information you manage directly such as app-specific account details. You can also include information from sources to which your app has approved access such as the Contacts framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/contactresolver/useridentity())*