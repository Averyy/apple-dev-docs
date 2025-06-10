# readerInstanceIdentifier

**Framework**: ProximityReader  
**Kind**: property

The unique identifier for the mobile document reader instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
let readerInstanceIdentifier: String
```

## Mentions

- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md)

#### Discussion

> **Note**: Do not cache this value. When generating a reader token always retrieve the latest reader instance identifier first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader/configuration-swift.struct/readerinstanceidentifier)*