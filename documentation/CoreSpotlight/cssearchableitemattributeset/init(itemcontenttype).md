# init(itemContentType:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Creates an attribute set for the specified content type.

**Availability**:
- iOS 9.0+ - Deprecated in 27.3
- iPadOS 9.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.3
- macOS 10.11+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`init(contentType:)`](./init%28contenttype%29.md) instead.

## Declaration

```swift
init(itemContentType: String)
```

```objc
- (instancetype) initWithItemContentType:(NSString *) itemContentType;
```

## Return Value

An attribute set that represents an item of the specified content type.

## Parameters

- `itemContentType`: The uniform type identifier of the content. For example, `kUTTypePNG` or `kUTTypeMovie`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/init(itemcontenttype:))*