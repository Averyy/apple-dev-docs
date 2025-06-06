# withCString(encodedAs:_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.

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
func withCString<Result, Encoding>(encodedAs targetEncoding: Encoding.Type, _ body: (UnsafePointer<Encoding.CodeUnit>) throws -> Result) rethrows -> Result where Encoding : _UnicodeEncoding
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(encodedAs:_:)`. Do not store or return the pointer for later use.

## Parameters

- `targetEncoding`: The encoding in which the code units should be   interpreted.
- `body`: A closure with a pointer parameter that points to a   null-terminated sequence of code units. If   has a return   value, that value is also used as the return value for the    method. The pointer argument is valid   only for the duration of the method’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/withcstring(encodedas:_:))*