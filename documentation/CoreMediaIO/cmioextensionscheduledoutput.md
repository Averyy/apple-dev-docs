# CMIOExtensionScheduledOutput

**Framework**: Core Media I/O  
**Kind**: class

An object that represents scheduled output.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionScheduledOutput
```

## Topics

### Creating a Scheduled Output
- [init(sequenceNumber: UInt64, hostTimeInNanoseconds: UInt64)](cmioextensionscheduledoutput/init(sequencenumber:hosttimeinnanoseconds:).md)
  Creates a scheduled output object.
### Inspecting the Output
- [var sequenceNumber: UInt64](cmioextensionscheduledoutput/sequencenumber.md)
  The buffer sequence number that was output.
- [var hostTimeInNanoseconds: UInt64](cmioextensionscheduledoutput/hosttimeinnanoseconds.md)
  The host time in nanoseconds when the buffer was output.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func notifyScheduledOutputChanged(CMIOExtensionScheduledOutput)](cmioextensionstream/notifyscheduledoutputchanged(_:).md)
  Notifies clients when a particular buffer is output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput)*