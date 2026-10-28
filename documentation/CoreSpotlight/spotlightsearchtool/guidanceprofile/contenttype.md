# contentType

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to determine matches using an item’s type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var contentType: Bool?
```

## Discussion

Set the value of this property to `true` to give the model the option to match items based on their `CSSearchableItemAttributes/contentType` attribute. If you don’t specify a value for this property, the default value is `false`.

## See Also

### Specifying the supported search techniques
- [var dates: Bool?](./dates.md)
  A Boolean value that indicates whether to determine matches using date or time values.
- [var numericMatch: Bool?](./numericmatch.md)
  A Boolean value that indicates whether to determine matches using numerical values.
- [var people: Bool?](./people.md)
  A Boolean value that indicates whether to determine matches using the presence of specific people.
- [var similarityMatch: Bool?](./similaritymatch.md)
  A Boolean value that indicates whether to perform semantic similarity matching on your content.
- [var textMatch: Bool?](./textmatch.md)
  A Boolean value that indicates whether to perform keyword-based text matching on your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile/contenttype)*