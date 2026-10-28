# propertyIsCached

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Type Property

This flag is set when the callback [`AudioFileStream_PropertyListenerProc`](../audiofilestream_propertylistenerproc.md) is invoked in the case that the value of the property has been cached and can be obtained later.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var propertyIsCached: AudioFileStreamPropertyFlags { get }
```

```c
kAudioFileStreamPropertyFlag_PropertyIsCached
```

## Discussion

If this flag is not set,  get the value of the property from within this callback or set the [`cacheProperty`](./cacheproperty.md) flag to instruct the parser to begin caching the property data. Otherwise, the value will not be available after the callback returns.

## See Also

### Constants
- [static var cacheProperty: AudioFileStreamPropertyFlags](./cacheproperty.md)
  A property listener sets this flag to instruct the parser to cache the property value so that it remains available after the callback returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/propertyiscached)*