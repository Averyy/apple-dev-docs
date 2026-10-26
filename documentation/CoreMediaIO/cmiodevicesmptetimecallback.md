# CMIODeviceSMPTETimeCallback

**Framework**: Core Media I/O  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
struct CMIODeviceSMPTETimeCallback
```

```c
struct CMIODeviceSMPTETimeCallback;
```

## Topics

### Initializers
- [init()](./cmiodevicesmptetimecallback/init%28%29.md)
- [init(mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!, mRefCon: UnsafeMutableRawPointer!)](./cmiodevicesmptetimecallback/init%28mgetsmptetimeproc,mrefcon%29.md)
### Instance Properties
- [var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!](./cmiodevicesmptetimecallback/mgetsmptetimeproc.md)
- [var mRefCon: UnsafeMutableRawPointer!](./cmiodevicesmptetimecallback/mrefcon.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct CMIODeviceAVCCommand](./cmiodeviceavccommand.md)
- [struct CMIODeviceRS422Command](./cmiodevicers422command.md)
- [struct CMIODeviceStreamConfiguration](./cmiodevicestreamconfiguration.md)
- [struct CMIOObjectPropertyAddress](./cmioobjectpropertyaddress.md)
- [struct CMIOStreamDeck](./cmiostreamdeck.md)
- [struct CMIOStreamScheduledOutputNotificationProcAndRefCon](./cmiostreamscheduledoutputnotificationprocandrefcon.md)
- [CMIOHardwarePlugInInterface](./cmiohardwareplugininterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmiodevicesmptetimecallback)*