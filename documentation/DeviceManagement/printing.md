# Printing

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures printers.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object Printing
```

#### Discussion

Specify `com.apple.mcxprinting` as the payload type.

Removing this profile from a device doesn’t automatically remove printers from the device.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>

            <key>RequireAdminToAddPrinters</key>
            <false/>
            <key>AllowLocalPrinters</key>
            <true/>
            <key>RequireAdminToPrintLocally</key>
            <true/>
            <key>ShowOnlyManagedPrinters</key>
            <true/>
            <key>PrintFooter</key>
            <true/>
            <key>PrintMACAddress</key>
            <true/>
            <key>FooterFontSize</key>
            <string>7</string>
            <key>FooterFontName</key>
            <string>Helvetica</string>
            <key>DefaultPrinter</key>
            <dict>
                <key>DeviceURI</key>
                <string>ipp://printer.example.com/</string>
                <key>DisplayName</key>
                <string>printer.example.com</string>
            </dict>
            <key>UserPrinterList</key>
            <dict>
                <key>printer_example_com</key>
                <dict>
                    <key>DeviceURI</key>
                    <string>ipp://printer.example.com/</string>
                    <key>DisplayName</key>
                    <string>printer.example.com</string>
                    <key>Location</key>
                    <string>My Office</string>
                    <key>Model</key>
                    <string>PrinterModel1</string>
                    <key>PrinterLocked</key>
                    <true/>
                    <key>PPDURL</key>
                    <string>file://localhost/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Resources/Generic.ppd</string>
                </dict>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.myprinterpayload</string>
            <key>PayloadType</key>
            <string>com.apple.mcxprinting</string>
            <key>PayloadUUID</key>
            <string>8242d870-95c0-0135-0b44-0c4de9ce4c04</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Printing</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>ab59f143-1478-419a-885e-7994fb13c9c3</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Printing.DefaultPrinter](printing/defaultprinter-data.dictionary.md)
  A default printer for the user.
- [object Printing.UserPrinterList](printing/userprinterlist-data.dictionary.md)
  A list of printer dictionaries.

## Properties

- `AllowLocalPrinters` (boolean): If `true`, allows printers that connect directly to a user’s computer.
- `DefaultPrinter` (Printing.DefaultPrinter): The default printer for the user.
- `FooterFontName` (string): The footer font name.
- `FooterFontSize` (string): The footer font size.
- `PrintFooter` (boolean): If `true`, prints the page footer (including the user name and date).
- `PrintMACAddress` (boolean): If `true`, includes the MAC address.
- `RequireAdminToAddPrinters` (boolean): If `true`, requires an administrator password to add printers.
- `RequireAdminToPrintLocally` (boolean): If `true`, requires an administrator password to print locally.
- `ShowOnlyManagedPrinters` (boolean): If `true`, shows only managed printers.
- `UserPrinterList` (Printing.UserPrinterList): The printers available to a user.

## See Also

- [object AirPrint](airprint.md)
  The payload that configures AirPrint printer discoverability in the user’s printer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/printing)*