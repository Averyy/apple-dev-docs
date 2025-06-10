# update(_:forFileAt:)

**Framework**: Core Spotlight  
**Kind**: method

Provides searchable attributes for a file at the specified URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func update(_ attributes: CSSearchableItemAttributeSet, forFileAt contentURL: URL) throws
```

#### Discussion

When Core Spotlight invokes this method, update the properties of the attribute set according to the content in the specified file. For a complete list of properties available, see [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md).

> ❗ **Important**:  Core Spotlight indexes files in batches and may call this method simultaneously on multiple queues with different values of `contentURL`.

## Parameters

- `attributes`: The attribute set for the file at  .
- `contentURL`: The URL of the file to provide attributes for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csimportextension/update(_:forfileat:))*