# withUnsafeBytes(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.

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
func withUnsafeBytes<E, Result>(_ body: (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, Result : ~Copyable
```

#### Return Value

The return value of the `body` closure parameter.

#### Discussion

The buffer pointer passed as an argument to `body` is valid only during the execution of `withUnsafeBytes(_:)`. Do not store or return the pointer for later use.

Note: For an empty `RawSpan`, the closure always receives a `nil` pointer.

## Parameters

- `body`: A closure with an    parameter that points to the viewed contiguous storage.   If   has a return value, that value is also   used as the return value for the   method.   The closure’s parameter is valid only for the duration of   its execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/withunsafebytes(_:))*