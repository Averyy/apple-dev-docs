# searchScopes

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The scope of the search in your app’s content.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
static var searchScopes: Self.Criteria.SearchScopes { get }
```

#### Discussion

Use this property to indicate the portions of your content the type searches. The type of this property depends on the search criteria you use. For example, if your app intent supports [`StringSearchCriteria`](stringsearchcriteria.md), the value of this type is an array of [`StringSearchScope`](stringsearchscope.md) values.

## See Also

- [enum StringSearchScope](stringsearchscope.md)
  Constants that help the system understand the in-app search functionality and its searchable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/showinappsearchresultsintent/searchscopes)*