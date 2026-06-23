# init(elements:)

**Framework**: Swift  
**Kind**: init

View a typed span as a raw span.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
init<Element>(elements span: Span<Element>) where Element : ConvertibleToBytes
```

#### Discussion

Creates a `RawSpan` over the memory represented by a `Span<Element>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/init(elements:))*