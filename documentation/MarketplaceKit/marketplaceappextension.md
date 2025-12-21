# MarketplaceAppExtension

**Framework**: MarketplaceKit  
**Kind**: protocol

An extension that facilitates authentication, installation, and launch of a marketplace with deep links.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol MarketplaceAppExtension : AppExtension, Sendable
```

## Mentions

- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)

#### Overview

You provide this extension to enable the operating system to facilitate some tasks for your app even if it isn’t running, such as:

- Automatically updating apps when a new version is available.
- Providing additional header text for communications with your marketplace server.
- Launching your app storefront for a specific app.
- Handling failures in requests to your marketplace server.

##### Define the Extension Point Identifier

To set up your marketplace extension in Xcode, use a generic extension template and set the `EXExtensionPointIdentifier` key in the `Info.plist` file to `com.apple.marketplace.extension`:

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
- [func additionalHeaders(for: URLRequest, account: String) async -> [String : String]](marketplaceappextension/additionalheaders(for:account:).md)
  Adds information to the request header for communications from the operating system to your marketplace endpoints.
- [func automaticUpdates(for: [AppVersion]) async throws -> [AutomaticUpdate]](marketplaceappextension/automaticupdates(for:).md)
- [func availableAppVersions(forAppleItemIDs: [AppleItemID]) async -> [AppVersion]](marketplaceappextension/availableappversions(forappleitemids:).md)
- [func requestFailed(response: HTTPURLResponse) async -> Bool](marketplaceappextension/requestfailed(response:).md)
  Handles when the operating system receives an unexpected response from your web server.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceappextension)*