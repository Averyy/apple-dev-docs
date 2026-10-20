# ProductIconPhase.failure(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The promotional image failed to load, with an error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case failure(any Error)
```

## Parameters

- `Error`: The reason that the promotional image failed to load.

## See Also

### Getting the promotional image’s load phases
- [ProductIconPhase.loading](./loading.md)
  The promotional image is in the process of loading.
- [ProductIconPhase.success(_:)](./success%28_%29.md)
  The promotional image successfully loaded.
- [ProductIconPhase.unavailable](./unavailable.md)
  The promotional image isn’t available for download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/producticonphase/failure(_:))*