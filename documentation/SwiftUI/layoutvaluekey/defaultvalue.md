# defaultValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The default value of the key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var defaultValue: Self.Value { get }
```

#### Discussion

Implement the `defaultValue` property for a type that conforms to the [`LayoutValueKey`](../layoutvaluekey.md) protocol. For example, you can create a `Flexibility` layout value that defaults to `nil`:

```swift
private struct Flexibility: LayoutValueKey {
    static let defaultValue: CGFloat? = nil
}
```

The type that you declare for the `defaultValue` sets the layout key’s [`Value`](./value.md) associated type. The Swift compiler infers the key’s associated type in the above example as an optional [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md).

Any view that you don’t explicitly set a value for uses the default value. Override the default value for a view using the [`layoutValue(key:value:)`](../view/layoutvalue%28key,value%29.md) modifier.

## See Also

### Providing a default value
- [associatedtype Value](./value.md)
  The type of the key’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutvaluekey/defaultvalue)*