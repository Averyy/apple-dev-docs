# buildPartialBlock(accumulated:next:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func buildPartialBlock<each Accumulated, R>(accumulated: ResolverSpecificationBuilder<Property>.Specification<Property, repeat each Accumulated>, next: R) -> ResolverSpecificationBuilder<Property>.Specification<Property, repeat each Accumulated, R> where repeat each Accumulated : Resolver, R : Resolver
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/buildpartialblock(accumulated:next:))*