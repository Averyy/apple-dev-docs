# mutableBytes

**Framework**: Swift  
**Kind**: property

Construct a mutable raw span over the memory represented by this span.

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
var mutableBytes: MutableRawSpan { mutating get }
```

#### Return Value

A `MutableRawSpan` over the memory represented by this span.

#### Discussion

Mutating `self` through this property is unsafe because it is possible to mutate a byte so as to produce an invalid bit pattern in the corresponding instance of `Element`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/mutablebytes-7cwoq)*