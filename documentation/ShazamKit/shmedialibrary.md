# SHMediaLibrary

**Framework**: ShazamKit  
**Kind**: class

An object that represents the user’s Shazam library.

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
class SHMediaLibrary
```

#### Overview

Use `SHMediaLibrary` to add matched songs from the Shazam catalog to the user’s Shazam library.

> **Note**:  There’s no system permission necessary to write to the user’s Shazam library. Consider requesting permission from the user before adding songs to the library.

## Topics

### Adding a matched song to the library
- [class var `default`: SHMediaLibrary](shmedialibrary/default.md)
  An instance of the user’s default Shazam library.
- [func add([SHMediaItem], completionHandler: ((any Error)?) -> Void)](shmedialibrary/add(_:completionhandler:).md)
  Adds an array of songs to the user’s Shazam library.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class SHLibrary](shlibrary.md)
  An object that represents a user’s synced Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmedialibrary)*