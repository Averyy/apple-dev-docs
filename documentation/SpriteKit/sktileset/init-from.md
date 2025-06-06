# init(from:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a tile set from a URL to an archived .sks file.

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
convenience init?(from url: URL)
```

#### Return Value

A new tile set or `nil` if the URL doesn’t point to a valid tile set file.

## Parameters

- `url`: The URL of a tile set file.

## See Also

- [convenience init?(named: String)](sktileset/init(named:).md)
  Initializes a tile set by searching the app bundle for an archived `.sks` file by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/init(from:))*