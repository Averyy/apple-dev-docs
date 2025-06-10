# AppDependency

**Framework**: App Intents  
**Kind**: class

A property wrapper that resolves a registered dependency at runtime.

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
@propertyWrapper
final class AppDependency<Value> where Value : Sendable
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)

## Topics

### Initializers
- [convenience init(key: AnyHashable?, manager: AppDependencyManager)](appdependency/init(key:manager:).md)
- [convenience init(key: AnyHashable?, manager: AppDependencyManager, default: () async throws -> Value)](appdependency/init(key:manager:default:)-226je.md)
- [convenience init(key: AnyHashable?, manager: AppDependencyManager, default: @autoclosure () -> Value)](appdependency/init(key:manager:default:)-wvhz.md)
### Instance Properties
- [var projectedValue: AppDependency<Value>](appdependency/projectedvalue.md)
- [var wrappedValue: Value](appdependency/wrappedvalue.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AppDependencyManager](appdependencymanager.md)
  An object that manages the registration and initialization of an app intent’s dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appdependency)*