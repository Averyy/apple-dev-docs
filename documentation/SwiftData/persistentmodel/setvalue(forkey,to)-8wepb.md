# setValue(forKey:to:)

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
func setValue<Value>(forKey: KeyPath<Self, Value>, to newValue: Value) where Value : PersistentModel
```

## See Also

### Modifying a value by key path
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](./setvalue%28forkey,to%29-18176.md)
- [func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to: Value)](./setvalue%28forkey,to%29-3mmp2.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value?>, to: Value?)](./setvalue%28forkey,to%29-3uqwc.md)
- [func setValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](./setvalue%28forkey,to%29-xt24.md)
- [func setTransformableValue<Value>(forKey: KeyPath<Self, Value>, to: Value)](./settransformablevalue%28forkey,to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentmodel/setvalue(forkey:to:)-8wepb)*