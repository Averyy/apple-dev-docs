# withUnsafeMutableBufferPointer(_:)

**Framework**: Swift  
**Kind**: method

Call a closure with a pointer to the viewed mutable contiguous storage.

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
mutating func withUnsafeMutableBufferPointer<E, Result>(_ body: (UnsafeMutableBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result where E : Error, Result : ~Copyable
```

#### Return Value

The return value of the `body` closure parameter.

#### Discussion

The buffer pointer passed as an argument to `body` is valid only during the execution of `withUnsafeMutableBufferPointer(_:)`. Do not store or return the pointer for later use.

## Parameters

- `body`: A closure with an `UnsafeMutableBufferPointer` parameter that points to the viewed contiguous storage. If `body` has a return value, that value is also used as the return value for the `withUnsafeMutableBufferPointer(_:)` method. The closure’s parameter is valid only for the duration of its execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/withunsafemutablebufferpointer(_:))*