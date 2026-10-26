# CMIODeviceAVCCommand

**Framework**: Core Media I/O  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
struct CMIODeviceAVCCommand
```

```c
struct CMIODeviceAVCCommand;
```

## Topics

### Initializers
- [init()](./cmiodeviceavccommand/init%28%29.md)
- [init(mCommand: UnsafeMutablePointer<UInt8>!, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>!, mResponseLength: UInt32, mResponseUsed: UInt32)](./cmiodeviceavccommand/init%28mcommand,mcommandlength,mresponse,mresponselength,mresponseused%29.md)
### Instance Properties
- [var mCommand: UnsafeMutablePointer<UInt8>!](./cmiodeviceavccommand/mcommand.md)
- [var mCommandLength: UInt32](./cmiodeviceavccommand/mcommandlength.md)
- [var mResponse: UnsafeMutablePointer<UInt8>!](./cmiodeviceavccommand/mresponse.md)
- [var mResponseLength: UInt32](./cmiodeviceavccommand/mresponselength.md)
- [var mResponseUsed: UInt32](./cmiodeviceavccommand/mresponseused.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct CMIODeviceRS422Command](./cmiodevicers422command.md)
- [struct CMIODeviceSMPTETimeCallback](./cmiodevicesmptetimecallback.md)
- [struct CMIODeviceStreamConfiguration](./cmiodevicestreamconfiguration.md)
- [struct CMIOObjectPropertyAddress](./cmioobjectpropertyaddress.md)
- [struct CMIOStreamDeck](./cmiostreamdeck.md)
- [struct CMIOStreamScheduledOutputNotificationProcAndRefCon](./cmiostreamscheduledoutputnotificationprocandrefcon.md)
- [CMIOHardwarePlugInInterface](./cmiohardwareplugininterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmiodeviceavccommand)*