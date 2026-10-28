# init(url:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a reference node from a URL.

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
convenience init(url referenceURL: URL)
```

```objc
+ (instancetype) referenceNodeWithURL:(NSURL *) referenceURL;
```

## Return Value

A newly initialized reference node.

## Discussion

This intializer is for loading archives that reside outside of the app bundle.

## Parameters

- `referenceURL`: The URL of the reference node.

## See Also

### Initializers
- [init(url: URL?)](./init%28url%29-429mo.md)
  Initializes a reference node from a URL.
- [convenience init(fileNamed: String)](./init%28filenamed%29-77gs0.md)
  Creates a reference node from a file in the app’s main bundle.
- [init(fileNamed: String?)](./init%28filenamed%29-2yeh2.md)
  Initializes a reference node from a file in the app’s main bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  A method that initializes a reference node from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreferencenode/init(url:)-3jryz)*