# AppToAppLayerVPNMapping.AppLayerVPNMappingItem.MatchToolsItem

**Framework**: Device Management  
**Kind**: dictionary

Specifies a per-app VPN rule to match network traffic that the app’s spawned command-line tool generates.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
object AppToAppLayerVPNMapping.AppLayerVPNMappingItem.MatchToolsItem
```

## Properties

- `DesignatedRequirement` (string) *(required)*: The code signature designated requirement of the command-line tool using the per-app VPN.
- `Path` (string): The file-system path of the command-line tool using the per-app VPN.
- `SigningIdentifier` (string) *(required)*: The code signature signing identifier of the command-line tool using the per-app VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apptoapplayervpnmapping/applayervpnmappingitem/matchtoolsitem)*