# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns an attribute value that a key path indicates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

#### Overview

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire discontiguous attributed substring. To find portions of an attributed string with consistent attributes, use the `runs` property. Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where n is the number of runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(dynamicmember:)-5i1c9)*