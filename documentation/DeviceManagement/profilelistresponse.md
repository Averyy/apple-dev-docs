# ProfileListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of installed profiles.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ProfileListResponse
```

## Topics

### Commands
- [object ProfileListResponse.ProfileListItem](profilelistresponse/profilelistitem.md)
  A dictionary that describes a profile list item.
- [object ProfileListResponse.ProfileListItem.PayloadContentItem](profilelistresponse/profilelistitem/payloadcontentitem.md)
  A dictionary that describes a profile payload content item.
- [object ProfileListResponse.ErrorChainItem](profilelistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## See Also

- [object ProfileListCommand](profilelistcommand.md)
  The command to get a list of installed profiles on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profilelistresponse)*