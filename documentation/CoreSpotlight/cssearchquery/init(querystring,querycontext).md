# init(queryString:queryContext:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Initializes and returns a query object with the specified query string and query context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(queryString: String, queryContext: CSSearchQueryContext?)
```

```objc
- (instancetype) initWithQueryString:(NSString *) queryString queryContext:(CSSearchQueryContext *) queryContext;
```

## Return Value

An initialized query object.

## Discussion

- queryString: A formatted string that defines the matching criteria to apply to indexed items. To learn how to construct a query string, see [Create a query string for your search](../searching-for-information-in-your-app.md#Create-a-query-string-for-your-search).

  This parameter must not be `nil`.

  - queryContext: A [`CSSearchQueryContext`](../cssearchquerycontext.md) object that focuses the query results.

## Discussion

After you create and initialize a query object, and call [`start()`](./start%28%29.md) to begin the query, you can’t update or reuse the query object for a new query.

## See Also

### Creating a query object
- [convenience init(queryString: String, attributes: [String]?)](./init%28querystring,attributes%29.md)
  Initializes and returns a query object with the specified query string and item attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/init(querystring:querycontext:))*