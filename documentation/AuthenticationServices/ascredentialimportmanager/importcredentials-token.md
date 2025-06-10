# importCredentials(token:)

**Framework**: Authentication Services  
**Kind**: method

Begins the credential import process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func importCredentials(token: UUID) async throws -> ASExportedCredentialData
```

#### Return Value

The credential data exported from the source app.

#### Discussion

When a person chooses your app to receive credentials exported from another app, the system launches your app using an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) of type `ASCredentialExchangeActivityType`. Handle this in your app delegate for AppKit/UIKit or the [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) modifier for SwiftUI. The `NSUserActivity` you receive contains a single [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) object in its `userInfo` field with the key `ASCredentialImportToken`; pass this UUID as the `token` parameter to this method.

This method throws an error if the import can’t proceed, which happens if the token doesn’t match what the system expects, indicating an app other than the one the export was meant for.

## Parameters

- `token`: The UUID token that the system provided in the   when launching the app.

## See Also

- [struct ASExportedCredentialData](asexportedcredentialdata.md)
  A container for credential data that your app provides to an exporter or receives from an importer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager/importcredentials(token:))*