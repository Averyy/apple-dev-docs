# defaultQuery

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The default query to use to retrieve entity property instances.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static var defaultQuery: Self.DefaultQuery { get }
```

## Mentions

- [Defining app entities for your custom data types](../defining-app-entities-for-your-custom-data-types.md)

## Discussion

You can create a query that uses identifier, name and more. For additional information, see [`Query`](../../SwiftData/query.md).

## Default Implementations

### AppEntity Implementations
- [static var defaultQuery: _RawRepresentableStringQuery<Self>](./defaultquery-3qobd.md)
- [static var defaultQuery: _TransientAppEntityQuery<Self>](./defaultquery-8vl7p.md)

## See Also

### Making the entity queryable
- [associatedtype DefaultQuery : EntityQuery](./defaultquery-swift.associatedtype.md)
- [static var defaultResolverSpecification: EmptyResolverSpecification<Self>](./defaultresolverspecification-2dpf2.md)
- [static var defaultResolverSpecification: some ResolverSpecification](./defaultresolverspecification-589eq.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity/defaultquery-4khg7)*