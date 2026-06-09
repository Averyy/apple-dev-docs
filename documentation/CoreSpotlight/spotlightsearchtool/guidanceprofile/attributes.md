# attributes

**Framework**: Core Spotlight  
**Kind**: property

The relevant attributes from your content that you want to search.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var attributes: [SearchableItemAttribute]?
```

#### Discussion

Use this property to specify only the attributes that are relevant for your content. If you provide a value for this property, the search tool considers only the attributes you specify. If you don’t specify a value for this property, or set the value to `nil`, all attributes are available during searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guidanceprofile/attributes)*