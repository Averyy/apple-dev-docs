# Query()

**Framework**: SwiftData  
**Kind**: macro  
**Role**: Macro

Fetches all instances of the attached model type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@attached(accessor)
@attached(peer, names: prefixed(`_`)) macro Query()
```

## See Also

### Model fetch
- [Filtering and sorting persistent data](./filtering-and-sorting-persistent-data.md)
  Manage data store presentation using predicates and dynamic queries.
- [Additional query macros](./additionalquerymacros.md)
  Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [struct Query](./query.md)
  A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [struct FetchDescriptor](./fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query())*