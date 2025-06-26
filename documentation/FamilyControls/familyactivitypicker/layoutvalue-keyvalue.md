# layoutValue(key:value:)

**Framework**: FamilyControls  
**Kind**: method

Associates a value with a custom layout property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func layoutValue<K>(key: K.Type, value: K.Value) -> some View where K : LayoutValueKey
```

#### Return Value

A view that has the specified value for the specified key.

#### Discussion

Use this method to set a value for a custom property that you define with `LayoutValueKey`. For example, if you define a `Flexibility` key, you can set the key on a `Text` view using the key’s type and a value:

```swift
Text("Another View")
    .layoutValue(key: Flexibility.self, value: 3)
```

For convenience, you might define a method that does this in an extension to `View`:

```swift
extension View {
    func layoutFlexibility(_ value: CGFloat?) -> some View {
        layoutValue(key: Flexibility.self, value: value)
    }
}
```

This method makes the call site easier to read:

```swift
Text("Another View")
    .layoutFlexibility(3)
```

If you perform layout operations in a type that conforms to the `Layout` protocol, you can read the key’s associated value for each subview of your custom layout type. Do this by indexing the subview’s proxy with the key. For more information, see `LayoutValueKey`.

## Parameters

- `key`: The type of the key that you want to set a value for.   Create the key as a type that conforms to the    protocol.
- `value`: The value to assign to the key for this view.   The value must be of the type that you establish for the key’s   associated value when you implement the key’s    property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/layoutvalue(key:value:))*