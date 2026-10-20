# putBytes

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

A pointer to a function that copies data to the data consumer. For more information, see [`CGDataConsumerPutBytesCallback`](../cgdataconsumerputbytescallback.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var putBytes: CGDataConsumerPutBytesCallback?
```

```c
CGDataConsumerPutBytesCallback putBytes;
```

## See Also

### Instance Properties
- [var releaseConsumer: CGDataConsumerReleaseInfoCallback?](./releaseconsumer.md)
  A pointer to a function that handles clean-up for the data consumer, or `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/putbytes)*