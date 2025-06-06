# url

**Framework**: Metal  
**Kind**: property

A URL to a Metal binary archive file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get set }
```

## Mentions

- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

#### Discussion

You can use this method to load a binary archive you created with an [`MTLBinaryArchive`](mtlbinaryarchive.md) instance’s [`serialize(to:)`](mtlbinaryarchive/serialize(to:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchivedescriptor/url)*