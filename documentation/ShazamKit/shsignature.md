# SHSignature

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SHSignature : NSObject
```

## Overview

You can save signatures to files and share them with others. Use saved signatures to populate a custom catalog.

Check whether your captured query signature is long enough to search for a match by comparing [`duration`](./shsignature/duration.md) to the [`minimumQuerySignatureDuration`](./shcatalog/minimumquerysignatureduration.md) and [`maximumQuerySignatureDuration`](./shcatalog/maximumquerysignatureduration.md) of a catalog.

For signatures longer than [`maximumQuerySignatureDuration`](./shcatalog/maximumquerysignatureduration.md), use [`slices(from:duration:stride:)`](./shsignature/slices%28from,duration,stride%29.md) to create multiple segments that meet the duration requirement.

## Topics

### Creating a signature object
- [init(dataRepresentation: Data) throws](./shsignature/init%28datarepresentation%29.md)
  Creates a signature object from raw data.
- [+ signatureWithDataRepresentation:error:](./shsignature/signaturewithdatarepresentation_error_.md)
  Creates a signature object from raw data.
### Reading signature information
- [var dataRepresentation: Data](./shsignature/datarepresentation.md)
  The raw data for the signature.
- [var duration: TimeInterval](./shsignature/duration.md)
  The duration of the audio you use to generate the signature.
### Slicing signature segments
- [func slices(from: TimeInterval, duration: TimeInterval, stride: TimeInterval?) throws -> SHSignature.Slices](./shsignature/slices%28from,duration,stride%29.md)
  Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.
- [SHSignature.Slices](./shsignature/slices.md)
  A sequence of signature segments.
### Getting the content type
- [static var shazamSignature: UTType](../UniformTypeIdentifiers/uttype-swift.struct/shazamsignature.md)
  A type that represents a signature.
- [SHSignatureContentType](../UniformTypeIdentifiers/uttype-c.class/shsignaturecontenttype.md)
  A type representing the @c SHSignature file format with the .shazamsignature extension
### Initializers
- [init?(coder: NSCoder)](./shsignature/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Create a signature from audio
- [class SHSignatureGenerator](./shsignaturegenerator.md)
  An object for converting audio data into a signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature)*