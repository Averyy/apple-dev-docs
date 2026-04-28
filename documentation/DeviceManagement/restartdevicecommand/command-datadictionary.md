# RestartDeviceCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to remotely and immediately restart a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- macOS 10.13+
- tvOS 10.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestartDeviceCommand.Command
```

## Properties

- `KextPaths` ([string]): If `RebuildKernelCache` is `true`, this value specifies the paths to kexts to add to the auxiliary kernel cache since the last kernel cache rebuild. If not present, the system only adds previously discovered kexts to the kernel cache. This value is available in macOS 11 and later.
- `NotifyUser` (boolean): If `true`, notifies the user to restart the device at their convenience. No forced restart occurs unless the device is at `loginwindow` with no logged-in users. The user can dismiss the notification and ignore the request. No further notifications display unless you resend the command. This value is available in macOS 11.3 and later.
- `RebuildKernelCache` (boolean): If `true`, the system rebuilds the kernel cache during a device restart. If `BootstrapTokenAllowedForAuthentication` is `true` in the [`SecurityInfoResponse.SecurityInfo`](securityinforesponse/securityinfo-data.dictionary.md) response, the device requests the bootstrap token from the MDM server prior to executing this command. This value is available in macOS 11 and later.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restartdevicecommand/command-data.dictionary)*