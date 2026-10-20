# init(named:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Returns the audio source associated with the specified filename.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
convenience init?(named fileName: String)
```

```objc
+ (instancetype) audioSourceNamed:(NSString *) fileName;
```

#### Return Value

An audio source object.

#### Discussion

This method looks in the system caches for an audio source with the specified name and returns that object if it exists. If a matching audio source is not already in the cache, this method locates the audio file with the specified name in the application’s main bundle, then creates a new audio source and caches it for reuse.

## Parameters

- `fileName`: The name of an audio file. If this filename has not been previously requested, the method looks for an audio file with the specified name in the application’s main bundle.

## See Also

### Creating an Audio Source
- [convenience init?(fileNamed: String)](./init%28filenamed%29.md)
  Initializes an audio source from an audio file in the application’s main bundle.
- [init?(url: URL)](./init%28url%29-3qyjs.md)
  Initializes an audio source from the specified audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/init(named:))*