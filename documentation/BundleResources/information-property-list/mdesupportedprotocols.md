# MDESupportedProtocols

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

A dictionary that declares which media sharing extension protocols an app supports.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Details

- **Name**: `MDESupportedProtocols`
- **Type**: dictionary

## Discussion

Add this key to your media app’s Info pane in Xcode to declare support for one or more media device extension protocols. Each dictionary entry maps a protocol identifier to an application identifier on the remote device:

```xml
<key>MDESupportedProtocols</key>
<dict>
    <key>com.example.sharingprotocol</key>
    <string>com.example.myapplicationidentifier</string>
</dict>
```

The dictionary key is the protocol’s [`UTTypeIdentifier`](./utexportedtypedeclarations/uttypeidentifier.md), matching the value declared in a media device extension’s [`UTExportedTypeDeclarations`](./utexportedtypedeclarations.md). The string value is the app identifier that the protocol launches on the remote device. The value can be empty when the protocol targets no specific remote application.

When a media device extension supporting one of the listed protocols is available on the system, or you set [`MDESupportsUniversalURLPlayback`](./mdesupportsuniversalurlplayback.md) to `true` and any URL-playback supporting extension is available on the system, [`supportedExtensionAvailable`](../../AVSystemRouting/avsystemroutecontroller-18ns8/supportedextensionavailable.md) returns `true` and your app can observe routing events through [`AVSystemRouteController`](../../AVSystemRouting/avsystemroutecontroller-18ns8.md).

Use the [`AVSystemRoute.LaunchMode.application`](../../AVSystemRouting/avsystemroute-5s2um/launchmode/application.md) launch mode to start your counterpart app on the remote device using the configured application identifier.

## See Also

### AVSystemRouting
- [MDESupportsUniversalURLPlayback](./mdesupportsuniversalurlplayback.md)
  A Boolean value that indicates whether an app supports URL-based playback via a media device extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportedprotocols)*