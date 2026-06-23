# init(_:)

**Framework**: Core Text  
**Kind**: init

Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ nsTextAlignment: NSTextAlignment)
```

#### Return Value

The Core Text alignment that corresponds to the value specified in `nsTextAlignment`.

#### Discussion

Use this function when you need to map between the UIKit and Core Text constants for text alignment.

## Parameters

- `nsTextAlignment`: The UIKit text alignment constant you want to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttextalignment/init(_:))*