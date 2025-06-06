# init(wrappedValue:_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.

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
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == Int
```

#### Discussion

A common usage is with enumerations:

```swift
enum MyEnum: Int {
    case a
    case b
    case c
}
struct MyView: View {
    @SceneStorage("MyEnumValue") private var value = MyEnum.a
    var body: some View { ... }
}
```

## Parameters

- `wrappedValue`: The default value if an integer value is not   available for the given key.
- `key`: A key used to save and restore the value.

## See Also

- [init(_:)](scenestorage/init(_:).md)
  Creates a property that can save and restore an Optional boolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:))*