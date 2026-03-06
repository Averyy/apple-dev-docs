# MEError

**Framework**: MediaExtension  
**Kind**: struct

A MediaExtension framework error.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MEError
```

#### Overview

If a [`MediaExtension`](MediaExtension.md) method fails, the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object contains an [`MEError`](meerror-swift.struct.md) instance that provides specific information about the failure.

## Topics

### Identifying the error domain and codes
- [static var allocationFailure: MEError.Code](meerror-swift.struct/allocationfailure.md)
  An error code that indicates the extension can’t allocate memory.
- [static var endOfStream: MEError.Code](meerror-swift.struct/endofstream.md)
  An error code that indicates the extension reached the end of the source file.
- [static var internalFailure: MEError.Code](meerror-swift.struct/internalfailure.md)
  An error code that indicates the extension encountered an internal operation failure, such as code loading.
- [static var invalidParameter: MEError.Code](meerror-swift.struct/invalidparameter.md)
  An error code that indicates the extension received an invalid parameter.
- [static var locationNotAvailable: MEError.Code](meerror-swift.struct/locationnotavailable.md)
  An error code that indicates a specific sample isn’t contiguous, spans more than one file, or is for some other reason unsuitable to read directly from a file.
- [static var noSamples: MEError.Code](meerror-swift.struct/nosamples.md)
  An error code that indicates there are no samples in the track or a request to load a sample buffer fails.
- [static var noSuchEdit: MEError.Code](meerror-swift.struct/nosuchedit.md)
  An error code that indicates the plug-in track reader received a request to return an edit that’s out of range.
- [static var parsingFailure: MEError.Code](meerror-swift.struct/parsingfailure.md)
  An error code that indicates the extension encountered an error while parsing the media.
- [static var permissionDenied: MEError.Code](meerror-swift.struct/permissiondenied.md)
  An error code that indicates the extension received a request to perform an invalid operation on a byte source.
- [static var propertyNotSupported: MEError.Code](meerror-swift.struct/propertynotsupported.md)
  An error code that indicates the extension encountered a property it doesn’t support reading and writing to.
- [static var referenceMissing: MEError.Code](meerror-swift.struct/referencemissing.md)
  An error code that indicates the decoder received a request to decode a sample without decoding the required reference frame dependencies first.
- [static var unsupportedFeature: MEError.Code](meerror-swift.struct/unsupportedfeature.md)
  An error code that indicates the extension doesn’t support an aspect of the media.
### Inspecting an error
- [var code: Int](../Foundation/NSError/code.md)
  The error code.
- [var errorCode: Int](../Foundation/CustomNSError/errorCode.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo.md)
  The user-info dictionary.
- [var hashValue: Int](../Swift/Hashable/hashValue.md)
  The hash value.
- [var userInfo: [String : Any]](../Foundation/NSError/userInfo.md)
  The user info dictionary.
- [static func == (lhs: Self, rhs: Self) -> Bool](../Swift/Equatable/==(_:_:)-3axv1.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](../Swift/Equatable/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into hasher: inout Hasher)](../Swift/Hashable/hash(into:)-v52.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [MEError.Code](meerror-swift.struct/code.md)
  An enumeration that models media extension error codes.
### Type Properties
- [static var errorDomain: String](meerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let MediaExtensionErrorDomain: String](mediaextensionerrordomain.md)
  The domain of the error.
- [MEError.Code](meerror-swift.struct/code.md)
  An enumeration that models media extension error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct)*