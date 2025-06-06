# ManagedApplicationListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get the status of all managed apps.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationListResponse
```

## Topics

### Commands
- [object ManagedApplicationListResponse.ManagedApplicationList](managedapplicationlistresponse/managedapplicationlist-data.dictionary.md)
  A dictionary that contains status information about managed apps.
- [object ManagedApplicationListResponse.ErrorChainItem](managedapplicationlistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## See Also

- [object ManagedApplicationListCommand](managedapplicationlistcommand.md)
  The command to get the status of managed apps on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationlistresponse)*