# error

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSError * error;
```

#### Discussion

The meaning of this property depends on the setting of the [`decodingFailurePolicy`](./decodingfailurepolicy-swift.property.md) property. For [`NSCoder.DecodingFailurePolicy.raiseException`](./decodingfailurepolicy-swift.enum/raiseexception.md), this property is always `nil`. For [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](./decodingfailurepolicy-swift.enum/seterrorandreturn.md), a non-`nil` value represents the first error encountered while decoding the archive.

## See Also

### Managing Decode Errors
- [func failWithError(any Error)](./failwitherror%28_%29.md)
  Signals to this coder that the decode operation has failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/error)*