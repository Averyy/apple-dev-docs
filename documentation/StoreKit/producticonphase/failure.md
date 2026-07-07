# ProductIconPhase.failure(_:)

**Framework**: StoreKit  
**Kind**: case

The promotional image failed to load, with an error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
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

- [ProductIconPhase.loading](producticonphase/loading.md)
  The promotional image is in the process of loading.
- [ProductIconPhase.success(_:)](producticonphase/success(_:).md)
  The promotional image successfully loaded.
- [ProductIconPhase.unavailable](producticonphase/unavailable.md)
  The promotional image isn’t available for download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/producticonphase/failure(_:))*