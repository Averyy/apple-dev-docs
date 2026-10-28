# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Initializes from the result of a previous call to `Path.stringRepresentation`. Fails if the `string` does not describe a valid path.

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
init?(_ string: String)
```

**Other overloads**:

```swift
init(_ callback: (inout Path) -> ())
```

```swift
init(_ path: CGMutablePath)
```

```swift
init(_ path: CGPath)
```

```swift
init(_ rect: CGRect)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/init(_:)-87w1j)*