# SHSignature

**Framework**: ShazamKit  
**Kind**: class

An object that contains the opaque data and other information for a signature.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class SHSignature
```

#### Overview

Save your signature to a file and share it with others by writing the data to a file. You can use the saved signatures of reference recordings to populate a custom catalog.

Check whether your captured query signature is long enough to search for a match by comparing [`duration`](shsignature/duration.md) to the [`minimumQuerySignatureDuration`](shcatalog/minimumquerysignatureduration.md) and [`maximumQuerySignatureDuration`](shcatalog/maximumquerysignatureduration.md) of a catalog.

## Topics

### Creating a signature object
- [init(dataRepresentation: Data) throws](shsignature/init(datarepresentation:).md)
  Creates a signature object from raw data.
### Reading signature information
- [var dataRepresentation: Data](shsignature/datarepresentation.md)
  The raw data for the signature.
- [var duration: TimeInterval](shsignature/duration.md)
  The duration of the audio you use to generate the signature.
### Slicing signature segments
- [func slices(from: TimeInterval, duration: TimeInterval, stride: TimeInterval?) throws -> SHSignature.Slices](shsignature/slices(from:duration:stride:).md)
  Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.
- [SHSignature.Slices](shsignature/slices.md)
  A sequence of signature segments.
### Getting the content type
- [static var shazamSignature: UTType](../UniformTypeIdentifiers/UTType-swift.struct/shazamSignature.md)
  A type that represents a signature.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SHSignatureGenerator](shsignaturegenerator.md)
  An object for converting audio data into a signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature)*