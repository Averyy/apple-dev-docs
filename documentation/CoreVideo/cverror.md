# CVError

**Framework**: Core Video  
**Kind**: struct

`CVError` wraps `CVReturn` values to present them as Swift Error values. This type is used for all errors thrown in the CoreVideo framework. All `CVReturn` values are provided as static constants.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct CVError
```

## Topics

### Initializers
- [init?(rawValue: CVReturn)](cverror/init(rawvalue:).md)
  Creates `CVError` with the given error code. Returns nil if `rawValue` is `kCVReturnSuccess`
### Instance Properties
- [var errorDescription: String?](cverror/errordescription.md)
  Localized messages describing the error.
### Type Properties
- [static let allocationFailed: CVError](cverror/allocationfailed.md)
  The allocation for a buffer or buffer pool failed. Most likely because of lack of resources.
- [static let internalError: CVError](cverror/internalerror.md)
  Error with an undetermined cause.
- [static let invalidArgument: CVError](cverror/invalidargument.md)
  At least one of the arguments passed in is not valid. Either out of range or the wrong type.
- [static let invalidPixelBufferAttributes: CVError](cverror/invalidpixelbufferattributes.md)
  A CVBuffer cannot be created with the given attributes.
- [static let invalidPixelFormat: CVError](cverror/invalidpixelformat.md)
  The requested pixel format is not supported for the CVBuffer type.
- [static let invalidPoolAttributes: CVError](cverror/invalidpoolattributes.md)
  A CVBufferPool cannot be created with the given attributes.
- [static let invalidSize: CVError](cverror/invalidsize.md)
  The requested size (most likely too big) is not supported for the CVBuffer type.
- [static let pixelBufferNotMetalCompatible: CVError](cverror/pixelbuffernotmetalcompatible.md)
  The Buffer cannot be used with Metal as either its size, pixel format or attributes are not supported by Metal.
- [static let poolAllocationFailed: CVError](cverror/poolallocationfailed.md)
  The allocation for the buffer pool failed. Most likely because of lack of resources. Check if your parameters are in range.
- [static let retry: CVError](cverror/retry.md)
  A scan hasn’t completely traversed the CVBufferPool due to a concurrent operation. The client can retry the scan.
- [static let unsupported: CVError](cverror/unsupported.md)
  This operation is unsupported on this data type.
- [static let wouldExceedAllocationThreshold: CVError](cverror/wouldexceedallocationthreshold.md)
  The allocation request failed because it would have exceeded a specified allocation threshold (see kCVPixelBufferPoolAllocationThresholdKey).
### Type Methods
- [static func check(CVReturn) throws(CVError)](cverror/check(_:).md)
  Throws an instance of `CVError` if `status` is not `kCVReturnSuccess`

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cverror)*