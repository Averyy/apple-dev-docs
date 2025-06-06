# init(queryString:attributes:)

**Framework**: Core Spotlight  
**Kind**: init

Initializes and returns a query object with the specified query string and item attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
convenience init(queryString: String, attributes: [String]?)
```

#### Return Value

An initialized query object.

#### Discussion

- queryString: A formatted string that defines the matching criteria to apply to indexed items. To learn how to construct a query string, see [`Create a query string for your search`](searching-for-information-in-your-app#Create-a-query-string-for-your-search.md). This parameter must not be `nil`. - attributes: An array of strings that represent the attributes of indexed items. Each string corresponds to a property name that your app can set for an item; for a list of possible properties, see [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md). Passing `nil` for this parameter means that the query doesn’t use attributes to find matching items.

#### Discussion

After you create and initialize a query object, and call [`start()`](cssearchquery/start().md) to begin the query, you can’t update or reuse the query object for a new query.

## See Also

- [init(queryString: String, queryContext: CSSearchQueryContext?)](cssearchquery/init(querystring:querycontext:).md)
  Initializes and returns a query object with the specified query string and query context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/init(querystring:attributes:))*