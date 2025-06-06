# init(from:)

**Framework**: ActivityKit  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitystate/init(from:))*