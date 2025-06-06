# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new Boolean value from the given string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(_ description: String)
```

#### Discussion

If the `description` value is any string other than `"true"` or `"false"`, the result is `nil`. This initializer is case sensitive.

## Parameters

- `description`: A string representation of the Boolean value.

## See Also

- [init(Bool)](bool/init(_:)-25sp9.md)
  Creates an instance equal to the given Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/init(_:)-83vgw)*