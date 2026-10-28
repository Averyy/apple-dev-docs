# CFRangeMake(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Declares and initializes a `CFRange` structure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFRangeMake(_ loc: CFIndex, _ len: CFIndex) -> CFRange
```

```c
static CFRange CFRangeMake(CFIndex loc, CFIndex len);
```

## Return Value

An initialized structure of type [`CFRange`](./cfrange.md).

## Discussion

This is an in-line convenience function for creating initialized [`CFRange`](./cfrange.md) structures.

## Parameters

- `loc`: The starting location of the range.
- `len`: The length of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrangemake(_:_:))*