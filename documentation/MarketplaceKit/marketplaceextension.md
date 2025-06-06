# MarketplaceExtension

**Framework**: MarketplaceKit  
**Kind**: protocol

An extension that facilitates authentication, installation, and launching a marketplace with deep links.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
protocol MarketplaceExtension : AppExtension, Sendable
```

## Mentions

- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)

#### Overview

You provide this extension to enable the operating system to facilitate some tasks for your app even if it isn’t running, such as:

- Automatically updating apps when a new version is available.
- Provide additional header text for communications with your marketplace server.
- Launching your app storefront for a specific app.
- Handling failures in requests to your marketplace server.

##### Define the Extension Point Identifier

To set up your marketplace extension in Xcode, use a generic extension template and set the `EXExtensionPointIdentifier` `Info.plist` key to  `com.apple.marketplace.extension`:

```None
<dict>
  <key>EXAppExtensionAttributes</key>
  <dict>
    <key>EXExtensionPointIdentifier</key>
    <string>com.apple.marketplace.extension</string>
  </dict>
</dict>
</plist>
```

## Topics

### Instance Methods
- [func additionalHeaders(for: URLRequest, account: String) -> [String : String]?](marketplaceextension/additionalheaders(for:account:).md)
  Adds information to the request header for communications from the operating system to your marketplace endpoints.
- [func automaticUpdates(for: [AppVersion]) async throws -> [AutomaticUpdate]](marketplaceextension/automaticupdates(for:).md)
- [func availableAppVersions(forAppleItemIDs: [AppleItemID]) -> [AppVersion]?](marketplaceextension/availableappversions(forappleitemids:).md)
- [func requestFailed(with: HTTPURLResponse) -> Bool](marketplaceextension/requestfailed(with:).md)
  Handles when iOS receives an unexpected response from your web server.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MarketplaceExtensionConfiguration](marketplaceextensionconfiguration.md)
  The type for a marketplace extension’s configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceextension)*