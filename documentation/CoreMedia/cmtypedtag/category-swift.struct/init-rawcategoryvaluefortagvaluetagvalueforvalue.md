# init(rawCategory:valueForTagValue:tagValueForValue:)

**Framework**: Core Media  
**Kind**: init

Creates a new tag category instance with defined mappings between a raw and typed tag value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(rawCategory: CMTypedTag<TypedValue>.RawCategory, valueForTagValue: @escaping (CMTag.Value) -> TypedValue?, tagValueForValue: @escaping (TypedValue) -> CMTag.Value)
```

#### Discussion

> ❗ **Important**:  To ensure that your category is valid, use an existing static category listed in [`Creating Typed Categories`](cmtypedtag/category-swift.struct#Creating-Typed-Categories.md) rather than creating an instance yourself.

## Parameters

- `rawCategory`: A raw 64-bit identifier for the category.
- `valueForTagValue`: A mapping from an internal tag value to a typed value.
- `tagValueForValue`: A mapping from a typed value to an internal value stored in the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag/category-swift.struct/init(rawcategory:valuefortagvalue:tagvalueforvalue:))*