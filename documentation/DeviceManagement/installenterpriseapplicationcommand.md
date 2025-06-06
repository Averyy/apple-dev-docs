# InstallEnterpriseApplicationCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to install an enterprise app on a device.

**Availability**:
- macOS 10.13.6+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object InstallEnterpriseApplicationCommand
```

#### Discussion

This command provides a more secure version of [`InstallApplicationCommand`](installapplicationcommand.md) that specifies a [`InstallEnterpriseApplicationCommand.Command.Manifest`](installenterpriseapplicationcommand/command-data.dictionary/manifest-data.dictionary.md) or [`ManifestURL`](manifesturl.md).

The request needs to contain either a `Manifest` or `ManifestURL`. When using `Manifest`, the system ignores pinning options. When using `ManifestURL`, it’s recommended to specify the pinning options to increase security.

In macOS, the system returns `Acknowledged` after it validates the parameters but before it downloads and installs the app. As a result, the system won’t report errors in the installation process to the MDM server.

## Topics

### Commands
- [object InstallEnterpriseApplicationCommand.Command](installenterpriseapplicationcommand/command-data.dictionary.md)
  The request dictionary to install an enterprise app.

## See Also

- [object InstallEnterpriseApplicationResponse](installenterpriseapplicationresponse.md)
  A response from the device after it processes the command to install an enterprise app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installenterpriseapplicationcommand)*