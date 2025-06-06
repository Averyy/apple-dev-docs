# SHCatalog

**Framework**: ShazamKit  
**Kind**: class

An abstract base class for storing reference signatures and their associated metadata.

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
class SHCatalog
```

#### Overview

This is the base class of your custom catalog.

## Topics

### Accessing catalog properties
- [var maximumQuerySignatureDuration: TimeInterval](shcatalog/maximumquerysignatureduration.md)
  The maximum duration of a query signature that you use to match reference signatures in the catalog.
- [var minimumQuerySignatureDuration: TimeInterval](shcatalog/minimumquerysignatureduration.md)
  The minimum duration of a query signature that you use to match reference signatures in the catalog.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SHCustomCatalog](shcustomcatalog.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Building a Custom Catalog and Matching Audio](building-a-custom-catalog-and-matching-audio.md)
  Display lesson content that’s synchronized to a learning video by matching the audio to a custom reference signature and associated metadata.
- [ShazamKit Dance Finder with Managed Session](shazamkit-dance-finder-with-managed-session.md)
  Find a video of dance moves for a specific song by matching the audio to a custom catalog, and show a history of recognized songs.
- [class SHCustomCatalog](shcustomcatalog.md)
  An object for storing the reference signatures for custom audio recordings and their associated metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcatalog)*