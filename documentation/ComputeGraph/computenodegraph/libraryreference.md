# ComputeNodeGraph.LibraryReference

**Framework**: Compute Graph  
**Kind**: struct

A Metal library and an optional bundle identifier that locates shader functions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
struct LibraryReference
```

#### Overview

Use `addLibrary(_:bundle:)` rather than constructing this type directly.

## Topics

### Initializers
- [init(library: any MTLLibrary, bundle: String?)](computenodegraph/libraryreference/init(library:bundle:).md)
### Instance Properties
- [var bundle: String?](computenodegraph/libraryreference/bundle.md)
  The bundle identifier used to scope shader function lookup, or `nil` if the library does not require one.
- [var library: any MTLLibrary](computenodegraph/libraryreference/library.md)
  The Metal library containing compiled shader functions.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/libraryreference)*