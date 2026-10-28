# init(initialValue:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates the published instance with an initial value.

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
init(initialValue: Value)
```

## Discussion

Don’t use this initializer directly. Instead, create a property with the `@Published` attribute, as shown here:

```swift
@Published var lastUpdated: Date = Date()
```

## Parameters

- `initialValue`: The publisher’s initial value.

## See Also

### Creating a published instance
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates the published instance with an initial wrapped value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/init(initialvalue:))*