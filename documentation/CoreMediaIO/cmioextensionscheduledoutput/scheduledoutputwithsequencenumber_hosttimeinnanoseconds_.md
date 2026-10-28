# scheduledOutputWithSequenceNumber:hostTimeInNanoseconds:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new scheduled output object.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) scheduledOutputWithSequenceNumber:(uint64_t) sequenceNumber hostTimeInNanoseconds:(uint64_t) hostTimeInNanoseconds;
```

## Return Value

A scheduled output object that describes the state of the stream.

## Parameters

- `sequenceNumber`: The buffer sequence number that was output.
- `hostTimeInNanoseconds`: The host time in nanoseconds when the buffer was output.

## See Also

### Creating a Scheduled Output
- [init(sequenceNumber: UInt64, hostTimeInNanoseconds: UInt64)](./init%28sequencenumber,hosttimeinnanoseconds%29.md)
  Creates a scheduled output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionscheduledoutput/scheduledoutputwithsequencenumber:hosttimeinnanoseconds:)*