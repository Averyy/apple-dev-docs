# merge(_:mergePolicy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Merges the container’s attributes with those in another attribute container.

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
mutating func merge(_ other: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew)
```

## Parameters

- `other`: The attribute container with the attributes to merge.
- `mergePolicy`: A policy to use when resolving conflicts between this string’s attributes and those in `other`.

## See Also

### Modifying Attributes
- [func merging(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy) -> AttributeContainer](./merging%28_,mergepolicy%29.md)
  Returns an attribute container by merging the container’s attributes with those in another attribute container.
- [AttributedString.AttributeMergePolicy](../attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/merge(_:mergepolicy:))*