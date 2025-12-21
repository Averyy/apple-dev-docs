# displayName

**Framework**: Authentication Services  
**Kind**: property

A user visible name for the identifier. For `app` types it will contain the localized name of the app. For `URL` types it will contain the host name of the URL if it contains a valid host. For `URL` type identifiers that do not contain a valid host and for `domain` type identifiers, this will be equal to `identifier`. This property is meant only as a best effort suggestion for display purposes. It is not used by the system to identify the service or suggest a credential for AutoFill.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
var displayName: String? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier/displayname)*