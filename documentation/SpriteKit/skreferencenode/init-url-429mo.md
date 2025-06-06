# init(url:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a reference node from a URL.

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
@MainActor
init(url: URL?)
```

#### Return Value

A newly initialized reference node.

#### Discussion

This intializer is for loading archives that reside outside of the app bundle.

## Parameters

- `url`: The URL of the reference node.

## See Also

- [convenience init(url: URL)](skreferencenode/init(url:)-3jryz.md)
  Creates a reference node from a URL.
- [convenience init(fileNamed: String)](skreferencenode/init(filenamed:)-77gs0.md)
  Creates a reference node from a file in the app’s main bundle.
- [init(fileNamed: String?)](skreferencenode/init(filenamed:)-2yeh2.md)
  Initializes a reference node from a file in the app’s main bundle.
- [init?(coder: NSCoder)](skreferencenode/init(coder:).md)
  A method that initializes a reference node from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreferencenode/init(url:)-429mo)*