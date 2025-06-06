# init(min:zero:full:max:)

**Framework**: Accelerate  
**Kind**: init

Returns a structure that describes the range and clamp limits for a pixel format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(min: CGFloat, zero: CGFloat, full: CGFloat, max: CGFloat)
```

#### Return Value

A structure that describes the range and clamp limits for a pixel format.

## Parameters

- `min`: The minimum encoded value.
- `zero`: The encoding for the value  .
- `full`: The encoding for   (  for chrominance).
- `max`: The maximum encoded value.

## See Also

- [init()](vimagechanneldescription/init.md)
  Returns an empty structure that describes the range and clamp limits for a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagechanneldescription/init(min:zero:full:max:))*