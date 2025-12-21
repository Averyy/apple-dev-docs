# AppStorage

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
@propertyWrapper struct AppStorage<Value>
```

## Topics

### Storing a value
- [init(wrappedValue:_:store:)](appstorage/init(wrappedvalue:_:store:).md)
  Creates a property that can save and restore tab sidebar customizations.
- [init(_:store:)](appstorage/init(_:store:).md)
  Creates a property that can read and write an Optional boolean user default.
### Getting the value
- [var wrappedValue: Value](appstorage/wrappedvalue.md)
- [var projectedValue: Binding<Value>](appstorage/projectedvalue.md)

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Restoring your app’s state with SwiftUI](restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [func defaultAppStorage(UserDefaults) -> some View](view/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [struct SceneStorage](scenestorage.md)
  A property wrapper type that reads and writes to persisted, per-scene storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage)*