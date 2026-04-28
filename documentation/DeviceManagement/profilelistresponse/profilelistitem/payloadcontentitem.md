# ProfileListResponse.ProfileListItem.PayloadContentItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a profile payload content item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ProfileListResponse.ProfileListItem.PayloadContentItem
```

## Properties

- `PayloadDescription` (string): A description of the payload.
- `PayloadDisplayName` (string): The human-readable name of the payload.
- `PayloadIdentifier` (string) *(required)*: The reverse-DNS-style identifier of the payload, such as `com.example.mypayload`.
- `PayloadOrganization` (string): The human-readable name of the organization that provided the payload.
- `PayloadType` (string) *(required)*: The type of payload, such as `com.apple.wifi.managed`.
- `PayloadUUID` (string) *(required)*: The unique identifier of the payload.
- `PayloadVersion` (integer) *(required)*: The version of the payload. The value is `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profilelistresponse/profilelistitem/payloadcontentitem)*