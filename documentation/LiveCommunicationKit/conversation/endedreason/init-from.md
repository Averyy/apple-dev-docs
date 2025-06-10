# init(from:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/endedreason/init(from:))*