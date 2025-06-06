# NSApplicationServices

**Framework**: Bundle Resources  
**Kind**: dictionary

A list of service providers and the devices that they support.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- watchOS 9.0+

#### Discussion

Use this key to define which devices [`DeviceDiscoveryUI`](https://developer.apple.com/documentation/DeviceDiscoveryUI) can connect with. The application services’s [`Browses`](information-property-list/nsapplicationservices/browses.md) key takes an array of dictionaries, where each dictionary contains a unique identifier, a usage description string, and a list of supported operating systems. You can define more than one application service for your apps. Each service has its own identifier, and can connect to a different subset of devices.

Set these in your tvOS app target’s Info tab, or in its `Info.plist` file.

```swift
<key>NSApplicationServices</key>
<dict>
    <key>Browses</key>
    <array>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Controller</string>
            <key>NSApplicationServiceUsageDescription</key>
            <string>You can control this app using an iOS device.</string>
            <key>NSApplicationServicePlatformSupport</key>
            <array>
                <string>iOS</string>
                <string>iPadOS</string>
            </array>
        </dict>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Workout</string>
            <key>NSApplicationServiceUsageDescription</key>
            <string>Connects to a watchOS app to read heart-rate and active calories burned from a workout session.</string>
            <key>NSApplicationServicePlatformSupport</key>
            <array>
                <string>watchOS</string>
            </array>
        </dict>
    </array>
</dict>
 
```

You can use the human-readable key names in Xcode’s property list editor.

![A screenshot showing the Application Services settings in Xcode’s property list editor.](https://docs-assets.developer.apple.com/published/cf9a6dfa9f67b5902bd2e32c0021352c/media-4030768%402x.png)

In the iOS, iPadOS, or watchOS app, use the [`Advertises`](information-property-list/nsapplicationservices/advertises.md) key, and give it an array of dictionaries where each dictionary lists the application service identifier for the connection types supported on this platform.

```swift
<key>NSApplicationServices</key>
<dict>
    <key>Advertises</key>
    <array>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Workout</string>
        </dict>
    </array>
</dict>

```

You can use the human-readable key names in Xcode’s property list editor.

![A screenshot showing the application services settings in Xcode’s property list editor.](https://docs-assets.developer.apple.com/published/caa062010907505ea9fffc771d37efd9/media-4030766%402x.png)

## Topics

### Property List Keys
- [Advertises](information-property-list/nsapplicationservices/advertises.md)
  An array of dictionaries, where each dictionary contains a unique identifier.
- [Browses](information-property-list/nsapplicationservices/browses.md)
  An array of dictionaries, where each dictionary contains a unique identifier, a usage description string, and a list of supported OSs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplicationservices)*