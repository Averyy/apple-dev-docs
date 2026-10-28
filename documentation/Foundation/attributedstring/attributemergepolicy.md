# AttributedString.AttributeMergePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

Use an [`AttributedString.AttributeMergePolicy`](./attributemergepolicy.md) when working with methods like [`mergeAttributes(_:mergePolicy:)`](./mergeattributes%28_,mergepolicy%29.md) to indicate how to resolve conflicts between multiple sets of attributes. When a source string and a merging attribute container both contain a given attribute with different values, the merge policy determines how to resolve the conflict.

## Topics

### Merge Policies
- [AttributedString.AttributeMergePolicy.keepCurrent](./attributemergepolicy/keepcurrent.md)
  A policy to keep the string’s current attribute value when merging multiple sets of attributes.
- [AttributedString.AttributeMergePolicy.keepNew](./attributemergepolicy/keepnew.md)
  A policy to keep the newly-merged attribute value when merging multiple sets of attributes.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying and Modifying Attributes
- [func setAttributes(AttributeContainer)](./setattributes%28_%29.md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](./mergeattributes%28_,mergepolicy%29.md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](./replaceattributes%28_,with%29.md)
  Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [protocol AttributedStringAttributeMutation](../attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/attributemergepolicy)*