# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Initialize a `Color` with a color resource.

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
init(_ resource: ColorResource)
```

**Other overloads**:

```swift
init(_ resolved: Color.Resolved)
```

```swift
init(_ resolved: Color.ResolvedHDR)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-1p49m)*