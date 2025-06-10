# init(data_desc:hidden_desc:cell_state_desc:)

**Framework**: Accelerate  
**Kind**: init

Returns a new long short-term memory (LSTM) data descriptor structure from the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(data_desc: BNNSNDArrayDescriptor, hidden_desc: BNNSNDArrayDescriptor, cell_state_desc: BNNSNDArrayDescriptor)
```

## Parameters

- `data_desc`: The descriptor of the input-output.
- `hidden_desc`: The descriptor of the hidden input-output.
- `cell_state_desc`: The descriptor of the cell-state input-output.

## See Also

- [init()](bnnslstmdatadescriptor/init.md)
  Returns a new long short-term memory (LSTM) data descriptor structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmdatadescriptor/init(data_desc:hidden_desc:cell_state_desc:))*