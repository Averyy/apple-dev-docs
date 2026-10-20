# SHMediaLibrary

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

An object that represents the user’s Shazam library.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use [`SHLibrary`](./shlibrary.md) instead.

## Declaration

```swift
class SHMediaLibrary
```

```objc
@interface SHMediaLibrary : NSObject
```

#### Overview

Use `SHMediaLibrary` to add matched songs from the Shazam catalog to the user’s Shazam library.

> **Note**:  There’s no system permission necessary to write to the user’s Shazam library. Consider requesting permission from the user before adding songs to the library.

## Topics

### Adding a matched song to the library
- [class var `default`: SHMediaLibrary](./shmedialibrary/default.md)
  An instance of the user’s default Shazam library.
- [func add([SHMediaItem], completionHandler: ((any Error)?) -> Void)](./shmedialibrary/add%28_,completionhandler%29.md)
  Adds an array of songs to the user’s Shazam library.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Update the user’s Shazam library
- [class SHLibrary](./shlibrary.md)
  An object that represents a user’s synced Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmedialibrary)*