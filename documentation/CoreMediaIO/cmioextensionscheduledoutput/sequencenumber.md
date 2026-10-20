# sequenceNumber

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The buffer sequence number that was output.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var sequenceNumber: UInt64 { get }
```

```objc
@property (atomic, readonly) uint64_t sequenceNumber;
```

## See Also

### Inspecting the Output
- [var hostTimeInNanoseconds: UInt64](./hosttimeinnanoseconds.md)
  The host time in nanoseconds when the buffer was output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput/sequencenumber)*