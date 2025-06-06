# kSCPropNetInterfaceSubType

**Framework**: System Configuration  
**Kind**: var

The Interface key `SubType`, whose value is of type `CFString`.

**Availability**:
- macOS 10.1+

## Declaration

```swift
let kSCPropNetInterfaceSubType: CFString
```

#### Discussion

This key can be passed the following constants when the `Type` key has the value `PPP`:

- `kSCValNetInterfaceSubTypePPPoE`, which has the value `PPPoE`
- `kSCValNetInterfaceSubTypePPPSerial`, which has the value `PPPSerial`
- `kSCValNetInterfaceSubTypePPTP`, which has the value `PPTP`
- `kSCValNetInterfaceSubTypeL2TP`, which has the value `L2TP`

## See Also

- [let kSCPropNetInterfaceDeviceName: CFString](kscpropnetinterfacedevicename-swift.var.md)
  The Interface key `DeviceName`, whose value is of type `CFString`.
- [let kSCPropNetInterfaceHardware: CFString](kscpropnetinterfacehardware-swift.var.md)
  The Interface key `Hardware`, whose value is of type `CFString`.
- [let kSCPropNetInterfaceType: CFString](kscpropnetinterfacetype-swift.var.md)
  The Interface key `Type`, whose value is of type `CFString`.
- [let kSCPropNetInterfaceSupportsModemOnHold: CFString](kscpropnetinterfacesupportsmodemonhold-swift.var.md)
  The Interface key `SupportsModemOnHold`, whose value is of type `CFNumber` and is equal to `0` or `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacesubtype-swift.var)*