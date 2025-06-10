# init()

**Framework**: Authentication Services  
**Kind**: init

Creates an import manager instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init()
```

#### Discussion

Create an instance of this class when the system launches your app with an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) of type `ASCredentialExchangeActivityType`, then call [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to import credentials from the source app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager/init())*