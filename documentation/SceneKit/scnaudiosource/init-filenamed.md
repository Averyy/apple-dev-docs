# init(fileNamed:)

**Framework**: SceneKit  
**Kind**: init

Initializes an audio source from an audio file in the application’s main bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(fileNamed name: String)
```

#### Return Value

A new audio source object.

#### Discussion

Calling this method is equivalent to using the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class to locate an audio file in the application’s main bundle and then passing the resulting URL to the [`init(url:)`](scnaudiosource/init(url:).md) method.

## Parameters

- `name`: The name of an audio file in the application’s main bundle.

## See Also

- [convenience init?(named: String)](scnaudiosource/init(named:).md)
  Returns the audio source associated with the specified filename.
- [init?(url: URL)](scnaudiosource/init(url:).md)
  Initializes an audio source from the specified audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/init(filenamed:))*