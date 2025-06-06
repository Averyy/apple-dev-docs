# releaseConsumer

**Framework**: Core Graphics  
**Kind**: property

A pointer to a function that handles clean-up for the data consumer, or `NULL`.

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
var releaseConsumer: CGDataConsumerReleaseInfoCallback?
```

#### Discussion

For more information, see [`CGDataConsumerReleaseInfoCallback`](cgdataconsumerreleaseinfocallback.md).

## See Also

- [var putBytes: CGDataConsumerPutBytesCallback?](cgdataconsumercallbacks/putbytes.md)
  A pointer to a function that copies data to the data consumer. For more information, see [`CGDataConsumerPutBytesCallback`](cgdataconsumerputbytescallback.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/releaseconsumer)*