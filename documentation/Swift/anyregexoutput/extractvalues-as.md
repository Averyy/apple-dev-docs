# extractValues(as:)

**Framework**: Swift  
**Kind**: method

Returns strongly-typed match output by converting this type-erased output to the specified type, if possible.

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
func extractValues<Output>(as outputType: Output.Type = Output.self) -> Output?
```

#### Return Value

The output, if the underlying value can be converted to `outputType`; otherwise, `nil`.

## Parameters

- `outputType`: The expected output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput/extractvalues(as:))*