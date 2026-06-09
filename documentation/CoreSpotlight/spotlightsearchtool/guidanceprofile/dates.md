# dates

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether to determine matches using date or time values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var dates: Bool?
```

#### Discussion

Set the value of this property to `true` to give the model the option to filter results based on date or time values. For example, you might enable this option if your items contain a start date or end date. If you don’t specify a value for this property, the default value is `false`.

## See Also

- [var contentType: Bool?](spotlightsearchtool/guidanceprofile/contenttype.md)
  A Boolean value that indicates whether to determine matches using an item’s type.
- [var numericMatch: Bool?](spotlightsearchtool/guidanceprofile/numericmatch.md)
  A Boolean value that indicates whether to determine matches using numerical values.
- [var people: Bool?](spotlightsearchtool/guidanceprofile/people.md)
  A Boolean value that indicates whether to determine matches using the presence of specific people.
- [var similarityMatch: Bool?](spotlightsearchtool/guidanceprofile/similaritymatch.md)
  A Boolean value that indicates whether to perform semantic similarity matching on your content.
- [var textMatch: Bool?](spotlightsearchtool/guidanceprofile/textmatch.md)
  A Boolean value that indicates whether to perform keyword-based text matching on your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile/dates)*