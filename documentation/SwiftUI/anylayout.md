# AnyLayout

**Framework**: SwiftUI  
**Kind**: struct

A type-erased instance of the layout protocol.

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
@frozen
struct AnyLayout
```

#### Overview

Use an `AnyLayout` instance to enable dynamically changing the type of a layout container without destroying the state of the subviews. For example, you can create a layout that changes between horizontal and vertical layouts based on the current Dynamic Type setting:

```swift
struct DynamicLayoutExample: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize <= .medium ?
            AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())

        layout {
            Text("First label")
            Text("Second label")
        }
    }
}
```

The types that you use with `AnyLayout` must conform to the [`Layout`](layout.md) protocol. The above example chooses between the [`HStackLayout`](hstacklayout.md) and [`VStackLayout`](vstacklayout.md) types, which are versions of the built-in [`HStack`](hstack.md) and [`VStack`](vstack.md) containers that conform to the protocol. You can also use custom layout types that you define.

## Topics

### Creating the layout
- [init<L>(L)](anylayout/init(_:).md)
  Creates a type-erased value that wraps the specified layout.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Layout](layout.md)

## See Also

- [struct HStackLayout](hstacklayout.md)
  A horizontal container that you can use in conditional layouts.
- [struct VStackLayout](vstacklayout.md)
  A vertical container that you can use in conditional layouts.
- [struct ZStackLayout](zstacklayout.md)
  An overlaying container that you can use in conditional layouts.
- [struct GridLayout](gridlayout.md)
  A grid that you can use in conditional layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anylayout)*