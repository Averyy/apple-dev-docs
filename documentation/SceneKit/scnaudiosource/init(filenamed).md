# init(fileNamed:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio source from an audio file in the application’s main bundle.

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
convenience init?(fileNamed name: String)
```

```objc
- (instancetype) initWithFileNamed:(NSString *) name;
```

## Return Value

A new audio source object.

## Discussion

Calling this method is equivalent to using the [`Bundle`](../../Foundation/bundle.md) class to locate an audio file in the application’s main bundle and then passing the resulting URL to the [`init(url:)`](./init%28url%29-3qyjs.md) method.

## Parameters

- `name`: The name of an audio file in the application’s main bundle.

## See Also

### Creating an Audio Source
- [convenience init?(named: String)](./init%28named%29.md)
  Returns the audio source associated with the specified filename.
- [init?(url: URL)](./init%28url%29-3qyjs.md)
  Initializes an audio source from the specified audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/init(filenamed:))*