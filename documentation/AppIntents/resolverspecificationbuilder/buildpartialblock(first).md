# buildPartialBlock(first:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func buildPartialBlock<R>(first: R) -> ResolverSpecificationBuilder<Property>.Specification<Property, R> where R : Resolver
```

Available when `Property` conforms to `_IntentValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/buildpartialblock(first:))*