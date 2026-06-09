# withCString(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.

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
func withCString<Result, E>(_ body: (UnsafePointer<CChar>) throws(E) -> Result) throws(E) -> Result where E : Error
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(_:)`. Do not store or return the pointer for later use.

## Parameters

- `body`: A closure with a pointer parameter that points to a null-terminated sequence of UTF-8 code units. If `body` has a return value, that value is also used as the return value for the `withCString(_:)` method. The pointer argument is valid only for the duration of the method’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/withcstring(_:))*