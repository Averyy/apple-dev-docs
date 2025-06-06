# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the capture with the specified name, if a capture with that name exists.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
subscript(name: String) -> AnyRegexOutput.Element? { get }
```

#### Return Value

An element providing information about the capture, if there is a capture named `name`; otherwise, `nil`.

## Parameters

- `name`: The name of the capture to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput/subscript(_:)-6qdcr)*