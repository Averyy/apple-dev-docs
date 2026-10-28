# init()

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

## Discussion

You don’t typically create an instance of [`EnvironmentValues`](../environmentvalues.md) directly. Doing so would provide access only to default values that don’t update based on system settings or device characteristics. Instead, you rely on an environment values’ instance that SwiftUI manages for you when you use the [`Environment`](../environment.md) property wrapper and the [`environment(_:_:)`](../view/environment%28_,_%29.md) view modifier.

## See Also

### Creating and accessing values
- [subscript(_:)](./subscript%28_%29.md)
  Accesses the environment value associated with a custom key.
- [var description: String](./description.md)
  A string that represents the contents of the environment values instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/init())*