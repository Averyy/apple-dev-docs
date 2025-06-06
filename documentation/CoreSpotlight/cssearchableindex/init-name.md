# init(name:)

**Framework**: Core Spotlight  
**Kind**: init

Returns an on-device index with the specified name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init(name: String)
```

#### Return Value

An on-device index.

#### Discussion

If you want to use batching or you want to index items in a specific protection class, you need to use your own index (you can’t perform batch updates on the default index).

## Parameters

- `name`: A name that pertains to your custom organization.

## See Also

- [class func `default`() -> Self](cssearchableindex/default.md)
  Returns the default on-device index.
- [init(name: String, protectionClass: FileProtectionType?)](cssearchableindex/init(name:protectionclass:).md)
  Returns an on-device index with the specified name and data protection class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/init(name:))*