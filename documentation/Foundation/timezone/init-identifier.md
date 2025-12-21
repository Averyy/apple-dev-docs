# init(identifier:)

**Framework**: Foundation  
**Kind**: init

Returns a time zone initialized with a given identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(identifier: String)
```

#### Discussion

An example identifier is “America/Los_Angeles”.

If `identifier` is an unknown identifier, then returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/init(identifier:))*