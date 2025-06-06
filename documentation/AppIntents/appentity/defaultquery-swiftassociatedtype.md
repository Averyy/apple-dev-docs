# DefaultQuery

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype DefaultQuery : EntityQuery where Self.ValueType == Self.DefaultQuery.Entity
```

## See Also

- [static var defaultQuery: Self.DefaultQuery](appentity/defaultquery-4khg7.md)
  The default query to use to retrieve entity property instances.
- [static var defaultResolverSpecification: EmptyResolverSpecification<Self>](appentity/defaultresolverspecification-2dpf2.md)
- [static var defaultResolverSpecification: some ResolverSpecification](appentity/defaultresolverspecification-589eq.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity/defaultquery-swift.associatedtype)*