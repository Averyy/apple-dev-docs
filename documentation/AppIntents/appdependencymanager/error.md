# AppDependencyManager.Error

**Framework**: App Intents  
**Kind**: enum

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
enum Error<Value>
```

## Topics

### Enumeration Cases
- [AppDependencyManager.Error.failedToLoadDependency(_:_:)](appdependencymanager/error/failedtoloaddependency(_:_:).md)
- [AppDependencyManager.Error.failedToRetrieveDependency(_:_:)](appdependencymanager/error/failedtoretrievedependency(_:_:).md)
- [case incorrectDependencyType(AnyHashable, Value.Type, any Any.Type)](appdependencymanager/error/incorrectdependencytype(_:_:_:).md)
### Instance Properties
- [var errorDescription: String?](appdependencymanager/error/errordescription.md)
  A localized message describing what error occurred.
### Default Implementations
- [Error Implementations](appdependencymanager/error/error-implementations.md)
- [LocalizedError Implementations](appdependencymanager/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appdependencymanager/error)*