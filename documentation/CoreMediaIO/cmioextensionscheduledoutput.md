# CMIOExtensionScheduledOutput

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that represents scheduled output.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionScheduledOutput
```

```objc
@interface CMIOExtensionScheduledOutput : NSObject
```

## Topics

### Creating a Scheduled Output
- [init(sequenceNumber: UInt64, hostTimeInNanoseconds: UInt64)](./cmioextensionscheduledoutput/init%28sequencenumber,hosttimeinnanoseconds%29.md)
  Creates a scheduled output object.
- [+ scheduledOutputWithSequenceNumber:hostTimeInNanoseconds:](./cmioextensionscheduledoutput/scheduledoutputwithsequencenumber_hosttimeinnanoseconds_.md)
  Returns a new scheduled output object.
### Inspecting the Output
- [var sequenceNumber: UInt64](./cmioextensionscheduledoutput/sequencenumber.md)
  The buffer sequence number that was output.
- [var hostTimeInNanoseconds: UInt64](./cmioextensionscheduledoutput/hosttimeinnanoseconds.md)
  The host time in nanoseconds when the buffer was output.
### Initializers
- [init?(coder: NSCoder)](./cmioextensionscheduledoutput/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Managing Scheduled Output
- [func notifyScheduledOutputChanged(CMIOExtensionScheduledOutput)](./cmioextensionstream/notifyscheduledoutputchanged%28_%29.md)
  Notifies clients when a particular buffer is output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput)*