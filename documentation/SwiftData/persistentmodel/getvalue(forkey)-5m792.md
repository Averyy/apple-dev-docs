# getValue(forKey:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

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
func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value where Value : RelationshipCollection, OtherModel == Value.PersistentElement
```

## See Also

### Accessing a value by key path
- [func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value](./getvalue%28forkey%29-299oe.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./getvalue%28forkey%29-3o59k.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./getvalue%28forkey%29-4cs0c.md)
- [func getValue<Value>(forKey: KeyPath<Self, Value?>) -> Value?](./getvalue%28forkey%29-998oq.md)
- [func getTransformableValue<Value>(forKey: KeyPath<Self, Value>) -> Value](./gettransformablevalue%28forkey%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentmodel/getvalue(forkey:)-5m792)*