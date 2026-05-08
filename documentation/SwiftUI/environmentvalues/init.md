# init()

**Framework**: SwiftUI  
**Kind**: init

Creates an environment values instance.

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
init()
```

#### Discussion

You don’t typically create an instance of [`EnvironmentValues`](environmentvalues.md) directly. Doing so would provide access only to default values that don’t update based on system settings or device characteristics. Instead, you rely on an environment values’ instance that SwiftUI manages for you when you use the [`Environment`](environment.md) property wrapper and the [`environment(_:_:)`](view/environment(_:_:).md) view modifier.

## See Also

- [subscript(_:)](environmentvalues/subscript(_:).md)
  Accesses the environment value associated with a custom key.
- [var description: String](environmentvalues/description.md)
  A string that represents the contents of the environment values instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/init())*