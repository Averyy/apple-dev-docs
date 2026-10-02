# includesTextListMarkers

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether TextKit includes text list markers in the text content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var includesTextListMarkers: Bool { get set }
```

#### Overview

When [`true`](https://developer.apple.com/documentation/swift/true), [`NSTextContentStorage`](nstextcontentstorage.md) assumes that a paragraph with an [`NSTextList`](nstextlist.md) includes the text list marker string.

This uses [`includesTextListMarkers`](nstextlist/includestextlistmarkers.md) to get a default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/includestextlistmarkers)*