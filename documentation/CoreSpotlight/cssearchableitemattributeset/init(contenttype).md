# init(contentType:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Creates an attribute set for the specified content type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(contentType: UTType)
```

```objc
- (instancetype) initWithContentType:(UTType *) contentType;
```

## Return Value

An attribute set that represents an item of the specified content type.

## Parameters

- `contentType`: The type of the content. For example, [`png`](../../UniformTypeIdentifiers/uttype-swift.struct/png.md) or [`movie`](../../UniformTypeIdentifiers/uttype-swift.struct/movie.md).

## See Also

### Creating an attribute set
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/init(contenttype:))*