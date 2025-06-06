# init(value:forProperty:)

**Framework**: Media Player  
**Kind**: init

Creates a media property predicate with the default comparison type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(value: Any?, forProperty property: String)
```

#### Return Value

A media property predicate.

#### Discussion

This is a convenience method that uses the default logical comparison type of [`MPMediaPredicateComparison.equalTo`](mpmediapredicatecomparison/equalto.md).

## Parameters

- `value`: The property value that you want to match when you query the Music library. For example, if you specify the   constant in the   parameter, in this parameter you supply a string containing the artist name.
- `property`: A property to use to build a media property predicate. See Media item types and keys.

## See Also

- [init(value: Any?, forProperty: String, comparisonType: MPMediaPredicateComparison)](mpmediapropertypredicate/init(value:forproperty:comparisontype:).md)
  Creates a media property predicate with a specified comparison type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/init(value:forproperty:))*