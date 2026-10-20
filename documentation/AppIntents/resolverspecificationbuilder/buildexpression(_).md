# buildExpression(_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

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
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
static func buildExpression<ResolverType>(_ expression: ResolverType) -> ResolverType where Property == ResolverType.Output, ResolverType : Resolver
```

Available when `Property` conforms to `_IntentValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/buildexpression(_:))*