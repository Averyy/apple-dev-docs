# init(entryCountPerSourceChannel:destinationChannelCount:data:)

**Framework**: Accelerate  
**Kind**: init

Returns a new multidimensional lookup table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<T>(entryCountPerSourceChannel: [UInt8], destinationChannelCount: Int, data: T) where T : AccelerateBuffer, T.Element == UInt16
```

#### Discussion

Supply the values in `data` in the range `0 ... 65535`, the function interprets the values as `0 ... 1` by dividing by `65535`.

## Parameters

- `entryCountPerSourceChannel`: An array that contains the number of table entries for each dimension of the lookup table.
- `destinationChannelCount`: The number of destination channels.
- `data`: The lookup table data. The lookup table must contain the product of the values in   multiplied by  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/init(entrycountpersourcechannel:destinationchannelcount:data:))*