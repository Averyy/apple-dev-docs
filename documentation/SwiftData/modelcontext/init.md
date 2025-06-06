# init(_:)

**Framework**: SwiftData  
**Kind**: init

Creates a context that belongs to the specified model container.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
init(_ container: ModelContainer)
```

#### Discussion

Use the context’s [`container`](modelcontext/container.md) property to access the model container after initializtion.

## Parameters

- `container`: The model container to associate with the initialized context.

## See Also

- [class ModelContainer](modelcontainer.md)
  An object that manages an app’s schema and model storage configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/init(_:))*