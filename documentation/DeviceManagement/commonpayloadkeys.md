# CommonPayloadKeys

**Framework**: Device Management  
**Kind**: dictionary

The properties common to all payloads.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
object CommonPayloadKeys
```

#### Discussion

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | N/A |

## Properties

- `PayloadDescription` (string): The human-readable description of this payload. This description appears on the Detail screen.
- `PayloadDisplayName` (string): The human-readable name for the profile payload. The name appears on the Detail screen and doesn’t need to be unique.
- `PayloadIdentifier` (string) *(required)*: The reverse-DNS-style identifier for the payload. This identifier is usually the same as the [`TopLevel`](toplevel.md) value, with an additional appended component. This string must be unique within the profile. During a profile replacement, the system updates payloads with the same `PayloadIdentifier` and `PayloadUUID` in the old and new profiles.
- `PayloadOrganization` (string): The human-readable string containing the name of the organization that provides the profile. This value doesn’t need to match the organization payload value in the enclosing dictionary.
- `PayloadType` (string) *(required)*: The payload type, which each payload domain’s reference page specifies.
- `PayloadUUID` (string) *(required)*: The globally unique identifier for the payload. The actual content is unimportant, but must be globally unique. In macOS, use `uuidgen` to generate UUIDs. During a profile replacement, the system updates payloads with the same `PayloadIdentifier` and `PayloadUUID` in the old and new profiles.
- `PayloadVersion` (integer) *(required)*: The version of this specific payload.

## See Also

- [object TopLevel](toplevel.md)
  The top-level payload properties for all profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/commonpayloadkeys)*