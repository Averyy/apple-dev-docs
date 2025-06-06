# Printing

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure printers.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Printing
```

#### Discussion

Specify `com.apple.mcxprinting` as the payload type.

Removing this profile from a device does not automatically remove printers from the device.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

##### Profile Example

```None
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
- [object Printing.UserPrinterList.Printer](printing/userprinterlist-data.dictionary/printer-data.dictionary.md)
  A printer dictionary.

## See Also

- [object AirPrint](airprint.md)
  The payload you use to configure AirPrint printers in the user’s printer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/printing)*