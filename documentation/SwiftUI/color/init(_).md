# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a constant color with the values specified by the resolved color.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ resolved: Color.Resolved)
```

**Other overloads**:

```swift
init(_ resolved: Color.ResolvedHDR)
```

```swift
init(_ resource: ColorResource)
```

```swift
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.Resolved
```

```swift
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.ResolvedHDR
```

```swift
init(_ cgColor: CGColor)
```

```swift
init(_ color: UIColor)
```

```swift
nonisolated
init(_ color: NSColor)
```

## See Also

### Creating a color
- [init(String, bundle: Bundle?)](./init%28_,bundle%29.md)
  Creates a color from a color set that you indicate by name.
- [func resolve(in: EnvironmentValues) -> Color.Resolved](./resolve%28in%29.md)
  Evaluates this color to a resolved color given the current `context`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:))*