# default

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Type Property

An instance of the user’s default Shazam library.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use SHLibrary instead

## Declaration

```swift
class var `default`: SHMediaLibrary { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (class, nonatomic, strong, readonly) SHMediaLibrary * defaultLibrary;
```

*macOS*

```objc
@property (class, atomic, strong, readonly) SHMediaLibrary * defaultLibrary;
```

## See Also

### Adding a matched song to the library
- [func add([SHMediaItem], completionHandler: ((any Error)?) -> Void)](./add%28_,completionhandler%29.md)
  Adds an array of songs to the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmedialibrary/default)*