# init(queryString:attributes:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Initializes and returns a query object with the specified query string and item attributes.

**Availability**:
- iOS 10.0+ - Deprecated in 16.0
- iPadOS 10.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.12+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use initWithQueryString:queryContext instead

## Declaration

```swift
convenience init(queryString: String, attributes: [String]?)
```

```objc
- (instancetype) initWithQueryString:(NSString *) queryString attributes:(NSArray<NSString *> *) attributes;
```

#### Return Value

An initialized query object.

#### Discussion

- queryString: A formatted string that defines the matching criteria to apply to indexed items. To learn how to construct a query string, see [Create a query string for your search](../searching-for-information-in-your-app.md#Create-a-query-string-for-your-search).

  This parameter must not be `nil`.

  - attributes: An array of strings that represent the attributes of indexed items. Each string corresponds to a property name that your app can set for an item; for a list of possible properties, see [`CSSearchableItemAttributeSet`](../cssearchableitemattributeset.md). Passing `nil` for this parameter means that the query doesn’t use attributes to find matching items.

#### Discussion

After you create and initialize a query object, and call [`start()`](./start%28%29.md) to begin the query, you can’t update or reuse the query object for a new query.

## See Also

### Creating a query object
- [init(queryString: String, queryContext: CSSearchQueryContext?)](./init%28querystring,querycontext%29.md)
  Initializes and returns a query object with the specified query string and query context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/init(querystring:attributes:))*