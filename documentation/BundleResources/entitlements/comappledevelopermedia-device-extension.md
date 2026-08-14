# com.apple.developer.media-device-extension

**Framework**: Bundle Resources  
**Kind**: typealias

An array of media sharing protocol identifiers that an extension supports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)



**Type**: string 

#### Discussion

Add this entitlement to your media device extension and its container app to integrate a third-party media sharing protocol into the system route picker. The entitlement’s value is an array of protocol identifiers using the `media-device-protocol.` prefix:

```xml
<key>com.apple.developer.media-device-extension</key>
<array>
    <string>media-device-protocol.myprotocol</string>
</array>
```

Each string must match a protocol identifier declared in the extension’s [`UTExportedTypeDeclarations`](information-property-list/utexportedtypedeclarations.md) and the [`protocolType`](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/protocoltype) property.

An app that holds this entitlement can’t hold any other managed entitlements.

Both the media device extension and its container app must declare this entitlement. The container app’s sole purpose must be the delivery and installation of the media device extension.

For more information, see [`Creating a media device extension`](https://developer.apple.com/documentation/mediadevice/creating-a-media-device-extension) and [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

## See Also

- [com.apple.developer.coremotion.head-pose](entitlements/com.apple.developer.coremotion.head-pose.md)
  An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.
- [com.apple.developer.spatial-audio.profile-access](entitlements/com.apple.developer.spatial-audio.profile-access.md)
  An entitlement that enables your app to use the personalized spatial audio profile.
- [com.apple.developer.avfoundation.multitasking-camera-access](entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md)
  A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.
- [Media Device Discovery Extension](entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.media-device-extension)*