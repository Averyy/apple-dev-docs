# init(url:name:)

**Framework**: Model I/O  
**Kind**: init

Initializes a texture that loads its texel data from a file at the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL, name: String?)
```

#### Return Value

A new URL-backed texture.

#### Discussion

This initializer does not load texel data from the URL; the [`MDLURLTexture`](mdlurltexture.md) class automatically loads data and caches it for reuse when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data.

## Parameters

- `URL`: The URL from which to load texture data.
- `name`: The   property for the new texture object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlurltexture/init(url:name:))*