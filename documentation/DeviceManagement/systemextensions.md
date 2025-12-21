# SystemExtensions

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures system extensions.

**Availability**:
- macOS 10.15+

## Declaration

```swift
object SystemExtensions
```

#### Discussion

Specify `com.apple.system-extension-policy` as the payload type.

When there are multiple installed profiles, the keys combine as follows:

- `AllowUserOverrides` is `false` if any profile sets it to `false`.
- All the other values combine together.

Beginning in macOS 11.3, installing or removing this payload can change the state of system extensions on the computer. If a containing application activates a system extension, and the system extension is in a pending state, installing a payload that allows the extension completes the activation process. If a system extension is active, removing a payload that allows the extension deactivates that extension.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | macOS |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowedExtensions</key>
            <array>
                <string>com.apple.share.System.send</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystemextensionpayload</string>
            <key>PayloadType</key>
            <string>com.apple.nsextension</string>
            <key>PayloadUUID</key>
            <string>3b378001-8cff-4bde-a6af-843fdb02f36d</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Extensions</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2e880ad8-e49e-47af-b416-7e6c3fba9df2</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object SystemExtensions.AllowedSystemExtensionTypes](systemextensions/allowedsystemextensiontypes-data.dictionary.md)
  A dictionary that maps team identifiers to system extensions.
- [object SystemExtensions.AllowedSystemExtensions](systemextensions/allowedsystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers that are allowed.
- [object SystemExtensions.NonRemovableFromUISystemExtensions](systemextensions/nonremovablefromuisystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.NonRemovableSystemExtensions](systemextensions/nonremovablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.RemovableSystemExtensions](systemextensions/removablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are removable.

## See Also

- [object Declarations](declarations.md)
  The payload that applies a set of declarations to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload that configures Energy Saver settings.
- [object FileProvider](fileprovider.md)
  The payload that configures file provider settings.
- [object Font](font.md)
  The payload that configures fonts.
- [object LockScreenMessage](lockscreenmessage.md)
  The payload that configures a Lock Screen message.
- [object Screensaver](screensaver.md)
  The payload that configures the screen saver.
- [object SystemLogging](systemlogging.md)
  The payload that configures system logging.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemextensions)*