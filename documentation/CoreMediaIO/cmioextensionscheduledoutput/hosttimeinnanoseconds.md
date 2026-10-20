# hostTimeInNanoseconds

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The host time in nanoseconds when the buffer was output.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var hostTimeInNanoseconds: UInt64 { get }
```

```objc
@property (atomic, readonly) uint64_t hostTimeInNanoseconds;
```

## See Also

### Inspecting the Output
- [var sequenceNumber: UInt64](./sequencenumber.md)
  The buffer sequence number that was output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput/hosttimeinnanoseconds)*