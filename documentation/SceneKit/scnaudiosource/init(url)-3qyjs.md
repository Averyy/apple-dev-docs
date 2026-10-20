# init(url:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio source from the specified audio file.

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
init?(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

#### Return Value

A new audio source object.

## Parameters

- `url`: A URL locating an audio file.

## See Also

### Creating an Audio Source
- [convenience init?(named: String)](./init%28named%29.md)
  Returns the audio source associated with the specified filename.
- [convenience init?(fileNamed: String)](./init%28filenamed%29.md)
  Initializes an audio source from an audio file in the application’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/init(url:)-3qyjs)*