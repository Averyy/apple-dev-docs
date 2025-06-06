# AttributedString.AttributeMergePolicy

**Framework**: Foundation  
**Kind**: enum

An enumeration of behaviors to apply when merging attributes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum AttributeMergePolicy
```

#### Overview

Use an [`AttributedString.AttributeMergePolicy`](attributedstring/attributemergepolicy.md) when working with methods like `AttributedString/mergeAttributes(_:mergePolicy:)` to indicate how to resolve conflicts between multiple sets of attributes. When a source string and a merging attribute container both contain a given attribute with different values, the merge policy determines how to resolve the conflict.

## Topics

### Merge Policies
- [AttributedString.AttributeMergePolicy.keepCurrent](attributedstring/attributemergepolicy/keepcurrent.md)
  A policy to keep the string’s current attribute value when merging multiple sets of attributes.
- [AttributedString.AttributeMergePolicy.keepNew](attributedstring/attributemergepolicy/keepnew.md)
  A policy to keep the newly-merged attribute value when merging multiple sets of attributes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AttributedStringAttributeMutation](attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/attributemergepolicy)*