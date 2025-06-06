# init(named:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a tile set by searching the app bundle for an archived `.sks` file by name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init?(named name: String)
```

#### Return Value

A new tile set or `nil` if a tile set with a matching name cannot be found.

## Parameters

- `name`: The name of the tile set to search for.

## See Also

- [convenience init?(from: URL)](sktileset/init(from:).md)
  Initializes a tile set from a URL to an archived .sks file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/init(named:))*