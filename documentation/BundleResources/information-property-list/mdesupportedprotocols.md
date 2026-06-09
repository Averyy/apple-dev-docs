# MDESupportedProtocols

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that declares which media sharing extension protocols an app supports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)



**Type**: dictionary

#### Discussion

Add this key to your media app’s Info pane in Xcode to declare support for one or more media device extension protocols. Each dictionary entry maps a protocol identifier to an application identifier on the remote device:

```xml
<key>MDESupportedProtocols</key>
<dict>
    <key>com.example.sharingprotocol</key>
    <string>com.example.myapplicationidentifier</string>
</dict>
```

The dictionary key is the protocol’s [`UTTypeIdentifier`](information-property-list/utexportedtypedeclarations/uttypeidentifier.md), matching the value declared in a media device extension’s [`UTExportedTypeDeclarations`](information-property-list/utexportedtypedeclarations.md). The string value is the app identifier that the protocol launches on the remote device. The value can be empty when the protocol targets no specific remote application.

When a media device extension supporting one of the listed protocols is available on the system, or you set [`MDESupportsUniversalURLPlayback`](information-property-list/mdesupportsuniversalurlplayback.md) to `true` and any URL-playback supporting extension is available on the system, [`supportedExtensionAvailable`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRouteController-18ns8/supportedExtensionAvailable) returns `true` and your app can observe routing events through [`AVSystemRouteController`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRouteController-18ns8).

Use the [`AVSystemRoute.LaunchMode.application`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um/LaunchMode/application) launch mode to start your counterpart app on the remote device using the configured application identifier.

## See Also

- [MDESupportsUniversalURLPlayback](information-property-list/mdesupportsuniversalurlplayback.md)
  A Boolean value that indicates whether an app supports URL-based playback via a media device extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportedprotocols)*