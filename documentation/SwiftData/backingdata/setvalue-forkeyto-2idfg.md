# setValue(forKey:to:)

**Framework**: SwiftData  
**Kind**: method  
**Required**: Yes

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
func setValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>, to newValue: Value) where Value : Encodable, Value : RelationshipCollection, OtherModel == Value.PersistentElement
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/backingdata/setvalue(forkey:to:)-2idfg)*