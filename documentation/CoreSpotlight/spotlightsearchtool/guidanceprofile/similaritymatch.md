# similarityMatch

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether to perform semantic similarity matching on your content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var similarityMatch: Bool?
```

#### Discussion

Set the value of this property true `true` to give the model the option to perform semantic searches of content. This approach allows the search to return results that match the intent of the provided string and not just the actual search term. For example, if model performs a semantic match against the word “star”, the tool can match items that contain the text “star”, “sun”, or “Betelgeuse”. If you don’t specify a value for this property, the default value is `false`.

## See Also

- [var contentType: Bool?](spotlightsearchtool/guidanceprofile/contenttype.md)
  A Boolean value that indicates whether to determine matches using an item’s type.
- [var dates: Bool?](spotlightsearchtool/guidanceprofile/dates.md)
  A Boolean value that indicates whether to determine matches using date or time values.
- [var numericMatch: Bool?](spotlightsearchtool/guidanceprofile/numericmatch.md)
  A Boolean value that indicates whether to determine matches using numerical values.
- [var people: Bool?](spotlightsearchtool/guidanceprofile/people.md)
  A Boolean value that indicates whether to determine matches using the presence of specific people.
- [var textMatch: Bool?](spotlightsearchtool/guidanceprofile/textmatch.md)
  A Boolean value that indicates whether to perform keyword-based text matching on your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile/similaritymatch)*