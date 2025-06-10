# defaultQuery

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The default query to use to retrieve entity property instances.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var defaultQuery: Self.DefaultQuery { get }
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Discussion

You can create a query that uses identifier, name and more. For additional information, see [`Query`](https://developer.apple.com/documentation/SwiftData/Query).

## See Also

- [associatedtype DefaultQuery : EntityQuery](appentity/defaultquery-swift.associatedtype.md)
- [static var defaultResolverSpecification: EmptyResolverSpecification<Self>](appentity/defaultresolverspecification-2dpf2.md)
- [static var defaultResolverSpecification: some ResolverSpecification](appentity/defaultresolverspecification-589eq.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity/defaultquery-4khg7)*