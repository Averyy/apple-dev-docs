# default()

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Type Method

Returns the default on-device index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> Self
```

```objc
+ (instancetype) defaultSearchableIndex;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

#### Return Value

The default on-device index.

#### Discussion

The default index doesn’t protect data or support batch updates, so use it only during prototyping or testing your Spotlight features. In your production code, create named indexes using [`init(name:)`](./init%28name%29.md) or [`init(name:protectionClass:)`](./init%28name,protectionclass%29.md) instead of using this index for your content.

## See Also

### Creating an index
- [init(name: String)](./init%28name%29.md)
  Returns an on-device index with the specified name.
- [init(name: String, protectionClass: FileProtectionType?)](./init%28name,protectionclass%29.md)
  Returns an on-device index with the specified name and data protection class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/default())*