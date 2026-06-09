# numericMatch

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether to determine matches using numerical values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var numericMatch: Bool?
```

#### Discussion

Set the value of this property to `true` to give the model the option to compare numerical values. For example, you might enable this option if your content contains Boolean attributes, star ratings, or any other attributes with numerical values. If you don’t specify a value for this property, the default value is `false`.

## See Also

- [var contentType: Bool?](spotlightsearchtool/guidanceprofile/contenttype.md)
  A Boolean value that indicates whether to determine matches using an item’s type.
- [var dates: Bool?](spotlightsearchtool/guidanceprofile/dates.md)
  A Boolean value that indicates whether to determine matches using date or time values.
- [var people: Bool?](spotlightsearchtool/guidanceprofile/people.md)
  A Boolean value that indicates whether to determine matches using the presence of specific people.
- [var similarityMatch: Bool?](spotlightsearchtool/guidanceprofile/similaritymatch.md)
  A Boolean value that indicates whether to perform semantic similarity matching on your content.
- [var textMatch: Bool?](spotlightsearchtool/guidanceprofile/textmatch.md)
  A Boolean value that indicates whether to perform keyword-based text matching on your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile/numericmatch)*