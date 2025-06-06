# init()

**Framework**: Authentication Services  
**Kind**: init

Creates an import manager instance.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
init()
```

#### Discussion

Create an instance of this class when the system launches your app with an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) of type `ASCredentialExchangeActivityType`, then call [`importCredentials(token:)`](ascredentialimportmanager/importcredentials(token:).md) to import credentials from the source app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager/init())*