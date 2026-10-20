# init(sequenceNumber:hostTimeInNanoseconds:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a scheduled output object.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(sequenceNumber: UInt64, hostTimeInNanoseconds: UInt64)
```

```objc
- (instancetype) initWithSequenceNumber:(uint64_t) sequenceNumber hostTimeInNanoseconds:(uint64_t) hostTimeInNanoseconds;
```

## Parameters

- `sequenceNumber`: The buffer sequence number that was output.
- `hostTimeInNanoseconds`: The host time in nanoseconds when the buffer was output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput/init(sequencenumber:hosttimeinnanoseconds:))*