# cacheProperty

**Framework**: Audio Toolbox  
**Kind**: property

A property listener sets this flag to instruct the parser to cache the property value so that it remains available after the callback returns.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var cacheProperty: AudioFileStreamPropertyFlags { get }
```

## See Also

- [static var propertyIsCached: AudioFileStreamPropertyFlags](audiofilestreampropertyflags/propertyiscached.md)
  This flag is set when the callback [`AudioFileStream_PropertyListenerProc`](audiofilestream_propertylistenerproc.md) is invoked in the case that the value of the property has been cached and can be obtained later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/cacheproperty)*