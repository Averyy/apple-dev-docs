# init(userQueryString:userQueryContext:)

**Framework**: Core Spotlight  
**Kind**: init

Creates a new user query that searches for the specified term.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(userQueryString: String?, userQueryContext: CSUserQueryContext?)
```

#### Return Value

An initialized query object.

## Parameters

- `userQueryString`: The term to search for. You may specify an empty string for this parameter.
- `userQueryContext`: A context object with options for how to run the query and generate results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/init(userquerystring:userquerycontext:))*