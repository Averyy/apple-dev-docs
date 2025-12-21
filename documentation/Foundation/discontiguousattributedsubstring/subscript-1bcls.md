# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns an attribute value that corresponds to an attributed string key.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

#### Overview

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire discontiguous attributed substring. To find portions of an attributed string with consistent attributes, use the `runs` property. Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where n is the number of runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-1bcls)*