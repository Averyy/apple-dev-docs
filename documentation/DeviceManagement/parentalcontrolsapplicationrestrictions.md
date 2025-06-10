# ParentalControlsApplicationRestrictions

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure parental controls for apps.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object ParentalControlsApplicationRestrictions
```

#### Discussion

Specify `com.apple.applicationaccess.new` as the payload type.

To determine if an app can be launched, the app is evaluated with these rules:

- Certain system app and utilities are always allowed to run.
- The allow list is searched to see if the `bundleID` has a matching entry. If a match is found, `appID` and `detachedSignature` (if present) are used to verify the signature of the app being launched. If the signature is valid and matches the designated requirement (in the appID key), the app is allowed to launch.
- If the path to the binary being launched matches or is in a subdirectory of a path in the deny list, the binary is denied.
- If the path to the binary being launched matches or is a subdirectory of a path in the allow list, the binary is allowed to launch.
- The binary is denied permission to launch.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
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
            <key>familyControlsEnabled</key>
            <true/>
            <key>pathBlackList</key>
            <array>
                <string>/Applications/Utilities</string>
            </array>
            <key>pathWhiteList</key>
            <array>
                <string>/Applications/Utilities</string>
            </array>
            <key>whiteList</key>
            <array>
                <dict>
                    <key>appID</key>
                    <data>+t4MAAAAADAAAAABAAAABgAAAAIAAAASY29tLmFwcGxlLlRleHRFZGl0AAAAAAAD</data>
                    <key>appStore</key>
                    <false/>
                    <key>bundleID</key>
                    <string>com.example.myotherapp</string>
                    <key>displayName</key>
                    <string>My App</string>
                    <key>subApps</key>
                    <array/>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myapplicationrestrictionspayload</string>
            <key>PayloadType</key>
            <string>com.apple.applicationaccess.new</string>
            <key>PayloadUUID</key>
            <string>e5af83ab-e936-495a-b6b7-05b113cf530e</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Parental Controls Application Restrictions</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>144fbebc-4db4-4642-83eb-78eed2992578</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ParentalControlsApplicationRestrictions.ApplicationItem](parentalcontrolsapplicationrestrictions/applicationitem.md)
  A dictionary defining an app for parental control.

## See Also

- [object ParentalControlsContentFilter](parentalcontrolscontentfilter.md)
  The payload you use to configure the parental control web content filters.
- [object ParentalControlsDictionary](parentalcontrolsdictionary.md)
  The payload you use to configure parental control dictionary restrictions.
- [object ParentalControlsGameCenter](parentalcontrolsgamecenter.md)
  The payload you use to configure Game Center parental controls.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload you use to configure parental control time limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsapplicationrestrictions)*