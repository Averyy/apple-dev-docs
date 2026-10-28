# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a constant color with the values specified by the resolved color.

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
init(_ resolved: Color.ResolvedHDR)
```

**Other overloads**:

```swift
init(_ resolved: Color.Resolved)
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

## Parameters

- `resolved`: The resolved color to initialize as the color’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-1hpum)*