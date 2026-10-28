# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color from a Core Graphics color.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(cgColor:)`](./init%28cgcolor%29.md) instead.

## Declaration

```swift
init(_ cgColor: CGColor)
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
init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.ResolvedHDR
```

```swift
init(_ color: UIColor)
```

```swift
nonisolated
init(_ color: NSColor)
```

## Parameters

- `cgColor`: A [`CGColor`](../../CoreGraphics/cgcolor.md) instance from which to create a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:)-1cwqj)*