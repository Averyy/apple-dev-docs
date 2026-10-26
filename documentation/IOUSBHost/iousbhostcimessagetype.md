# IOUSBHostCIMessageType

**Framework**: IOUSBHost  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostCIMessageType
```

```c
typedef enum { ... } IOUSBHostCIMessageType;
```

## Topics

### Initializers
- [init(UInt32)](./iousbhostcimessagetype/init%28_%29.md)
- [init(rawValue: UInt32)](./iousbhostcimessagetype/init%28rawvalue%29.md)
### Constants
- [var IOUSBHostCIMessageTypeCommandMax: IOUSBHostCIMessageType](./iousbhostcimessagetypecommandmax.md)
- [var IOUSBHostCIMessageTypeCommandMin: IOUSBHostCIMessageType](./iousbhostcimessagetypecommandmin.md)
- [var IOUSBHostCIMessageTypeControllerCapabilities: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollercapabilities.md)
- [var IOUSBHostCIMessageTypeControllerFrameNumber: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollerframenumber.md)
- [var IOUSBHostCIMessageTypeControllerPause: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollerpause.md)
- [var IOUSBHostCIMessageTypeControllerPowerOff: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollerpoweroff.md)
- [var IOUSBHostCIMessageTypeControllerPowerOn: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollerpoweron.md)
- [var IOUSBHostCIMessageTypeControllerStart: IOUSBHostCIMessageType](./iousbhostcimessagetypecontrollerstart.md)
- [var IOUSBHostCIMessageTypeDeviceCreate: IOUSBHostCIMessageType](./iousbhostcimessagetypedevicecreate.md)
- [var IOUSBHostCIMessageTypeDeviceDestroy: IOUSBHostCIMessageType](./iousbhostcimessagetypedevicedestroy.md)
- [var IOUSBHostCIMessageTypeDevicePause: IOUSBHostCIMessageType](./iousbhostcimessagetypedevicepause.md)
- [var IOUSBHostCIMessageTypeDeviceStart: IOUSBHostCIMessageType](./iousbhostcimessagetypedevicestart.md)
- [var IOUSBHostCIMessageTypeDeviceUpdate: IOUSBHostCIMessageType](./iousbhostcimessagetypedeviceupdate.md)
- [var IOUSBHostCIMessageTypeEndpointCreate: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointcreate.md)
- [var IOUSBHostCIMessageTypeEndpointDestroy: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointdestroy.md)
- [var IOUSBHostCIMessageTypeEndpointPause: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointpause.md)
- [var IOUSBHostCIMessageTypeEndpointReset: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointreset.md)
- [var IOUSBHostCIMessageTypeEndpointSetNextTransfer: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointsetnexttransfer.md)
- [var IOUSBHostCIMessageTypeEndpointUpdate: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpointupdate.md)
- [var IOUSBHostCIMessageTypeEndpoint_reserved_: IOUSBHostCIMessageType](./iousbhostcimessagetypeendpoint_reserved_.md)
- [var IOUSBHostCIMessageTypeFrameNumberUpdate: IOUSBHostCIMessageType](./iousbhostcimessagetypeframenumberupdate.md)
- [var IOUSBHostCIMessageTypeFrameTimestampUpdate: IOUSBHostCIMessageType](./iousbhostcimessagetypeframetimestampupdate.md)
- [var IOUSBHostCIMessageTypeIsochronousTransfer: IOUSBHostCIMessageType](./iousbhostcimessagetypeisochronoustransfer.md)
- [var IOUSBHostCIMessageTypeLink: IOUSBHostCIMessageType](./iousbhostcimessagetypelink.md)
- [var IOUSBHostCIMessageTypeNormalTransfer: IOUSBHostCIMessageType](./iousbhostcimessagetypenormaltransfer.md)
- [var IOUSBHostCIMessageTypePortCapabilities: IOUSBHostCIMessageType](./iousbhostcimessagetypeportcapabilities.md)
- [var IOUSBHostCIMessageTypePortDisable: IOUSBHostCIMessageType](./iousbhostcimessagetypeportdisable.md)
- [var IOUSBHostCIMessageTypePortEvent: IOUSBHostCIMessageType](./iousbhostcimessagetypeportevent.md)
- [var IOUSBHostCIMessageTypePortPowerOff: IOUSBHostCIMessageType](./iousbhostcimessagetypeportpoweroff.md)
- [var IOUSBHostCIMessageTypePortPowerOn: IOUSBHostCIMessageType](./iousbhostcimessagetypeportpoweron.md)
- [var IOUSBHostCIMessageTypePortReset: IOUSBHostCIMessageType](./iousbhostcimessagetypeportreset.md)
- [var IOUSBHostCIMessageTypePortResume: IOUSBHostCIMessageType](./iousbhostcimessagetypeportresume.md)
- [var IOUSBHostCIMessageTypePortStatus: IOUSBHostCIMessageType](./iousbhostcimessagetypeportstatus.md)
- [var IOUSBHostCIMessageTypePortSuspend: IOUSBHostCIMessageType](./iousbhostcimessagetypeportsuspend.md)
- [var IOUSBHostCIMessageTypeSetupTransfer: IOUSBHostCIMessageType](./iousbhostcimessagetypesetuptransfer.md)
- [var IOUSBHostCIMessageTypeStatusTransfer: IOUSBHostCIMessageType](./iousbhostcimessagetypestatustransfer.md)
- [var IOUSBHostCIMessageTypeTransferComplete: IOUSBHostCIMessageType](./iousbhostcimessagetypetransfercomplete.md)
### Instance Properties
- [var rawValue: UInt32](./iousbhostcimessagetype/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Enumerations
- [Anonymous](./api-3612464-anonymous.md)
- [Anonymous](./api-3612465-anonymous.md)
- [Anonymous](./api-3612466-anonymous.md)
- [Anonymous](./api-3612467-anonymous.md)
- [Anonymous](./api-3612468-anonymous.md)
- [Anonymous](./api-3612469-anonymous.md)
- [Anonymous](./api-3612470-anonymous.md)
- [Anonymous](./api-3612471-anonymous.md)
- [Anonymous](./api-3612472-anonymous.md)
- [Anonymous](./api-3612473-anonymous.md)
- [Anonymous](./api-3612474-anonymous.md)
- [Anonymous](./api-3612475-anonymous.md)
- [Anonymous](./api-3612476-anonymous.md)
- [Anonymous](./api-3612477-anonymous.md)
- [Anonymous](./api-3612478-anonymous.md)
- [IOUSBHostCIControllerState](./iousbhostcicontrollerstate.md)
- [IOUSBHostCIDeviceSpeed](./iousbhostcidevicespeed.md)
- [IOUSBHostCIDeviceState](./iousbhostcidevicestate.md)
- [IOUSBHostCIEndpointState](./iousbhostciendpointstate.md)
- [IOUSBHostCIExceptionType](./iousbhostciexceptiontype.md)
- [IOUSBHostCILinkState](./iousbhostcilinkstate.md)
- [IOUSBHostCIMessageStatus](./iousbhostcimessagestatus.md)
- [IOUSBHostCIPortState](./iousbhostciportstate.md)
- [IOUSBHostCIUserClientVersion](./iousbhostciuserclientversion.md)
- [IOUSBHostIsochronousTransactionOptions](./iousbhostisochronoustransactionoptions.md)
- [IOUSBHostIsochronousTransferOptions](./iousbhostisochronoustransferoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcimessagetype)*