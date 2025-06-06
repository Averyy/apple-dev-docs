# withCString(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

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
func withCString<Result>(_ body: (UnsafePointer<CChar>) throws -> Result) rethrows -> Result
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(_:)`. Do not store or return the pointer for later use.

## Parameters

- `body`: A closure with a pointer parameter that points to a   null-terminated sequence of UTF-8 code units. If   has a return   value, that value is also used as the return value for the    method. The pointer argument is valid only for the   duration of the method’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/withcstring(_:))*