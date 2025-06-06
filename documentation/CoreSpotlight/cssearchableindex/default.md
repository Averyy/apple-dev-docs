# default()

**Framework**: Core Spotlight  
**Kind**: method

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

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Return Value

The default on-device index.

#### Discussion

If you want to use batching or you want to index items in a specific protection class, you need to use your own index (you can’t perform batch updates on the default index).

## See Also

- [init(name: String)](cssearchableindex/init(name:).md)
  Returns an on-device index with the specified name.
- [init(name: String, protectionClass: FileProtectionType?)](cssearchableindex/init(name:protectionclass:).md)
  Returns an on-device index with the specified name and data protection class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/default())*