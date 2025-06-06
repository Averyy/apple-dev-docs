# withAAEncodedData(_:)

**Framework**: Apple Archive  
**Kind**: method

Executes a closure with encoded data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func withAAEncodedData<R>(_ body: (UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R
```

## Parameters

- `body`: The closure the function executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/withaaencodeddata(_:))*