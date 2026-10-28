# init(fileNamed:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a reference node from a file in the app’s main bundle.

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
convenience init(fileNamed fileName: String)
```

```objc
+ (instancetype) referenceNodeWithFileNamed:(NSString *) fileName;
```

## Return Value

A newly initialized reference node.

## Discussion

This initializer is for loading files that reside inside of the app bundle.

## Parameters

- `fileName`: The name of a file stored in the app’s main bundle.

## See Also

### Initializers
- [convenience init(url: URL)](./init%28url%29-3jryz.md)
  Creates a reference node from a URL.
- [init(url: URL?)](./init%28url%29-429mo.md)
  Initializes a reference node from a URL.
- [init(fileNamed: String?)](./init%28filenamed%29-2yeh2.md)
  Initializes a reference node from a file in the app’s main bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  A method that initializes a reference node from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreferencenode/init(filenamed:)-77gs0)*