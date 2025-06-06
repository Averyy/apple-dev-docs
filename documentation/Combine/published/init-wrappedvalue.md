# init(wrappedValue:)

**Framework**: Combine  
**Kind**: init

Creates the published instance with an initial wrapped value.

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
init(wrappedValue: Value)
```

#### Discussion

Don’t use this initializer directly. Instead, create a property with the `@Published` attribute, as shown here:

```swift
@Published var lastUpdated: Date = Date()
```

## Parameters

- `wrappedValue`: The publisher’s initial value.

## See Also

- [init(initialValue: Value)](published/init(initialvalue:).md)
  Creates the published instance with an initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/init(wrappedvalue:))*