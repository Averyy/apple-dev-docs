# ContainerValues

**Framework**: SwiftUI  
**Kind**: struct

A collection of container values associated with a given view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ContainerValues
```

#### Overview

SwiftUI exposes a collection of values associated with each view in the `ContainerValues` structure.

Container values you set on a given view affect only that view. Like preferences, container values are able to be read by views above the view they’re set on. Unlike preferences, however, container values don’t have merging behavior because they don’t escape their closest container. In the following example, the container value is set on the contained view, but is dropped when it reaches the containing [`VStack`](vstack.md).

```swift
VStack {
    Text("A")
        .containerValue(\.myCustomValue, 1) // myCustomValue = 1
    Text("B")
        .containerValue(\.myCustomValue, 2) // myCustomValue = 2
    // container values are unaffected by views that aren't containers:
    Text("C")
        .containerValue(\.myCustomValue, 3)
        .padding() // myCustomValue = 3
} // myCustomValue = it's default value, values do not escape the container
```

Even if a stack has only one child, container values still won’t be readable outside of the `VStack`. Container values don’t escape a container even if the container has only one child.

In this example, a direct subview writes a container value, allowing its direct container view to read it back:

```swift
@ViewBuilder var content: some View {
    Text("A")
        .containerValue(\.myCustomValue, 1)
}

ForEach(subviews: content) { subview in
    Text("value = \(subview.containerValues.myCustomValue)") // shows "value = 1"
}
```

However in the next example, the wrapping `VStack` means the `Text` view is not a direct subview of the outer container, so that container cannot read the changed value:

```swift
@ViewBuilder var containedContent: some View {
    VStack {
        Text("A")
            .containerValue(\.myCustomValue, 1)
    }
}

ForEach(subviews: containedContent) { subviews in
    Text("value = \(subview.containerValues.myCustomValue)") // shows the default value
}
```

Create a custom container value by declaring a new property in an extension to the container values structure and applying the [`Entry()`](entry().md) macro to the variable declaration:

```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

Clients of your value then access the value by reading it from the container values collection of a [`Subview`](subview.md).

Related pieces of container configuration can also be grouped under the same container values key.

```swift
struct PinPosition {
    var rotation: Double = 0
    var xOffset: Int = 0
}

extension ContainerValues {
    @Entry var pinPosition: PinPosition = .init()
}

// pinPosition.rotation = 0, pinPosition.xOffset = 3
Text("A").containerValue(\.pinPosition.xOffset, 3)

// pinPosition.rotation = 10, pinPosition.xOffset = 5
Text("B")
    .containerValue(\.pinPosition.rotation, 10)
    .containerValue(\.pinPosition.xOffset, 5)
```

This allows you to group multiple related container values into structs while maintaining separate modifiers to write each value.

```swift
extension View {
    func pinRotation(_ rotation: Double) -> some View {
        containerValue(\.pinPosition.rotation, rotation)
    }

    func pinXOffset(_ xOffset: Int) -> some View {
        containerValue(\.pinPosition.xOffset, xOffset)
    }
}
```

## Topics

### Instance Methods
- [func hasTag<V>(V) -> Bool](containervalues/hastag(_:).md)
  Returns true if the container values contain a tag matching a given value.
- [func tag<V>(for: V.Type) -> V?](containervalues/tag(for:).md)
  The tag value for the given type if the container values contains one.
### Subscripts
- [subscript<Key>(Key.Type) -> Key.Value](containervalues/subscript(_:).md)
  Accesses the particular container value associated with a custom key.

## See Also

- [struct Subview](subview.md)
  An opaque value representing a subview of another view.
- [struct SubviewsCollection](subviewscollection.md)
  An opaque collection representing the subviews of view.
- [struct SubviewsCollectionSlice](subviewscollectionslice.md)
  A slice of a SubviewsCollection.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](view/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [protocol ContainerValueKey](containervaluekey.md)
  A key for accessing container values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containervalues)*