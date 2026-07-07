# ComputeNodeGraph.LibraryReference

**Framework**: Compute Graph  
**Kind**: struct

A Metal library and an optional bundle identifier that locates shader functions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/libraryreference)*