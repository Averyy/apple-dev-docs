# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a path from an immutable shape path.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ path: CGPath)
```

**Other overloads**:

```swift
init(_ callback: (inout Path) -> ())
```

```swift
init(_ path: CGMutablePath)
```

```swift
init(_ rect: CGRect)
```

```swift
init?(_ string: String)
```

## Parameters

- `path`: The immutable CoreGraphics path to initialize the new path from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(_:)-3n5fl)*