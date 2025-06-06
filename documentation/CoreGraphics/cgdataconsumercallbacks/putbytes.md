# putBytes

**Framework**: Core Graphics  
**Kind**: property

A pointer to a function that copies data to the data consumer. For more information, see [`CGDataConsumerPutBytesCallback`](cgdataconsumerputbytescallback.md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var putBytes: CGDataConsumerPutBytesCallback?
```

## See Also

- [var releaseConsumer: CGDataConsumerReleaseInfoCallback?](cgdataconsumercallbacks/releaseconsumer.md)
  A pointer to a function that handles clean-up for the data consumer, or `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/putbytes)*