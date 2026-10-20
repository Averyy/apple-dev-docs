# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript

Access the `i`th element of the raw array pointed to by `self`.

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
subscript(i: Int) -> Pointee { get }
```

#### Overview

> **Precondition**: `self != nil`.

## See Also

### Accessing a Pointer’s Memory
- [var pointee: Pointee](./pointee.md)
  Retrieve or set the `Pointee` instance referenced by `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/subscript(_:))*