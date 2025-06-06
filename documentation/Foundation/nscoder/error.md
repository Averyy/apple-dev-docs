# error

**Framework**: Foundation  
**Kind**: property

An error in the top-level encode.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The meaning of this property depends on the setting of the [`decodingFailurePolicy`](nscoder/decodingfailurepolicy-swift.property.md) property. For [`NSCoder.DecodingFailurePolicy.raiseException`](nscoder/decodingfailurepolicy-swift.enum/raiseexception.md), this property is always `nil`. For [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md), a non-`nil` value represents the first error encountered while decoding the archive.

## See Also

- [func failWithError(any Error)](nscoder/failwitherror(_:).md)
  Signals to this coder that the decode operation has failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/error)*