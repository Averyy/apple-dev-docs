# systemVersion

**Framework**: Foundation  
**Kind**: property

The system version in effect for the archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var systemVersion: UInt32 { get }
```

#### Discussion

During encoding, the current version. During decoding, the version that was in effect when the data was encoded.

Subclasses that implement decoding must override this property to return the system version of the data being decoded.

## See Also

- [func version(forClassName: String) -> Int](nscoder/version(forclassname:).md)
  This method is present for historical reasons and is not used with keyed archivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/systemversion)*