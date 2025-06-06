# BackingData

**Framework**: SwiftData  
**Kind**: protocol

An interface for providing in-memory storage for a persistent model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
protocol BackingData<Model>
```

## Topics

### Associated Types
- [associatedtype Model : PersistentModel](backingdata/model.md)
### Initializers
- [init(for: Self.Model.Type)](backingdata/init(for:).md)
### Instance Properties
- [var metadata: Any](backingdata/metadata.md)
- [var persistentModelID: PersistentIdentifier?](backingdata/persistentmodelid.md)
### Instance Methods
- [func getTransformableValue<Value>(forKey: KeyPath<Self.Model, Value>) -> Value](backingdata/gettransformablevalue(forkey:).md)
- [func getValue<Value>(forKey: KeyPath<Self.Model, Value>) -> Value](backingdata/getvalue(forkey:)-1pric.md)
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>) -> Value](backingdata/getvalue(forkey:)-209t6.md)
- [func getValue<Value>(forKey: KeyPath<Self.Model, Value>) -> Value](backingdata/getvalue(forkey:)-5fis7.md)
- [func getValue<Value>(forKey: KeyPath<Self.Model, Value?>) -> Value?](backingdata/getvalue(forkey:)-5fo8.md)
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>) -> Value](backingdata/getvalue(forkey:)-8xj5n.md)
- [func setTransformableValue<Value>(forKey: KeyPath<Self.Model, Value>, to: Value)](backingdata/settransformablevalue(forkey:to:).md)
- [func setValue<Value>(forKey: KeyPath<Self.Model, Value>, to: Value)](backingdata/setvalue(forkey:to:)-1mr4x.md)
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>, to: Value)](backingdata/setvalue(forkey:to:)-2idfg.md)
- [func setValue<Value>(forKey: KeyPath<Self.Model, Value>, to: Value)](backingdata/setvalue(forkey:to:)-4d7yr.md)
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>, to: Value)](backingdata/setvalue(forkey:to:)-992es.md)
- [func setValue<Value>(forKey: KeyPath<Self.Model, Value?>, to: Value?)](backingdata/setvalue(forkey:to:)-rzi4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/backingdata)*