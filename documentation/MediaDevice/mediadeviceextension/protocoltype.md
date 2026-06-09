# protocolType

**Framework**: Media Device  
**Kind**: property  
**Required**: Yes

The communication protocol that this extension implements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var protocolType: UTType { get }
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Declaring the Protocol Type

Declare a custom Uniform Type Identifier in your extension’s Info.plist using `UTExportedTypeDeclarations`. The type must conform to `public.media-sharing-protocol`:

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.example.sharingprotocol</string>
        <key>UTTypeDescription</key>
        <string>My Sharing Protocol</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>public.media-sharing-protocol</string>
        </array>
        <key>UTTypeIcons</key>
		<dict>
			<key>UTTypeSymbolName</key>
			<string>sharingprotocol.logo</string>
		</dict>
    </dict>
</array>
```

- `UTTypeIdentifier`: A reverse-DNS string that uniquely identifies your protocol. Media apps receive this value through `AVSystemRoute/protocolType` and use it to determine which protocol is active.
- `UTTypeDescription`: A human-readable name for the protocol. The system may display this in user interfaces such as the route picker.
- `UTTypeConformsTo`: Must include `public.media-sharing-protocol`.

#### Returning the Type

Return a `UTType` whose identifier matches the `UTTypeIdentifier` declared in Info.plist:

```swift
var protocolType: UTType {
    UTType("com.example.sharingprotocol")!
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/protocoltype)*