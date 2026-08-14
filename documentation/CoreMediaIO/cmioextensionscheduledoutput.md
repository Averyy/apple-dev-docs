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
### Initializers
- [init?(coder: NSCoder)](cmioextensionscheduledoutput/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func notifyScheduledOutputChanged(CMIOExtensionScheduledOutput)](cmioextensionstream/notifyscheduledoutputchanged(_:).md)
  Notifies clients when a particular buffer is output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput)*