# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the element at `position`.

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
subscript(position: Base.Index) -> Element { get }
```

Available when `Base` conforms to `Collection`.

#### Overview

> **Precondition**: `position` is a valid position in `self` and `position != endIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/subscript(_:)-36b2w)*