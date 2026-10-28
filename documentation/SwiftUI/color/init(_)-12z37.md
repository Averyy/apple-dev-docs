# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color from a `ShapeStyle` instance that resolves to a custom color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.ResolvedHDR
```

**Other overloads**:

```swift
init(_ resolved: Color.Resolved)
```

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
init(_ cgColor: CGColor)
```

```swift
init(_ color: UIColor)
```

```swift
nonisolated
init(_ color: NSColor)
```

## Parameters

- `color`: The shape style value to initialize as the color’s provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-12z37)*