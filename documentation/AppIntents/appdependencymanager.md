# AppDependencyManager

**Framework**: App Intents  
**Kind**: class

An object that manages the registration and initialization of an app intent’s dependencies.

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
final class AppDependencyManager
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

## Topics

### Initializers
- [init()](appdependencymanager/init.md)
  Can be used to initialize a standalone `AppDependencyManager` for dependency injection during testing.
### Instance Methods
- [func add<Dependency>(key: AnyHashable?, dependency: @autoclosure () -> () throws -> Dependency)](appdependencymanager/add(key:dependency:)-1hqkg.md)
- [func add<Dependency>(key: AnyHashable?, dependency: @autoclosure () -> Dependency)](appdependencymanager/add(key:dependency:)-2le3x.md)
- [func add<Dependency>(key: AnyHashable?, dependency: () async throws -> Dependency)](appdependencymanager/add(key:dependency:)-gth5.md)
### Type Properties
- [static var shared: AppDependencyManager](appdependencymanager/shared.md)
### Enumerations
- [AppDependencyManager.Error](appdependencymanager/error.md)

## See Also

- [class AppDependency](appdependency.md)
  A property wrapper that resolves a registered dependency at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appdependencymanager)*