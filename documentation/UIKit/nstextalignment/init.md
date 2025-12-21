# init(_:)

**Framework**: UIKit  
**Kind**: init

Converts a Core Text alignment constant value to the matching constant value in UIKit.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ ctTextAlignment: CTTextAlignment)
```

#### Return Value

The UIKit text alignment that corresponds to the value specified in `ctTextAlignment`.

#### Discussion

Use this function when you need to map between the Core Text and UIKit constants for text alignment.

## Parameters

- `ctTextAlignment`: The Core Text alignment constant to convert.

## See Also

- [init(NSTextAlignment)](../CoreText/CTTextAlignment/init(_:).md)
  Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextalignment/init(_:))*