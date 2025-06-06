# init(value:forProperty:comparisonType:)

**Framework**: Media Player  
**Kind**: init

Creates a media property predicate with a specified comparison type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(value: Any?, forProperty property: String, comparisonType: MPMediaPredicateComparison)
```

#### Return Value

A media property predicate.

## Parameters

- `value`: The property value that you want to match when you query the Music library. For example, if you specify the   constant in the   parameter, in this parameter you supply a string containing the artist name.
- `property`: A property to use to build a media property predicate. See General Media Item Property Keys and Podcast Item Property Keys in  .
- `comparisonType`: : The logical comparison type for the predicate. See  .

## See Also

- [init(value: Any?, forProperty: String)](mpmediapropertypredicate/init(value:forproperty:).md)
  Creates a media property predicate with the default comparison type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/init(value:forproperty:comparisontype:))*