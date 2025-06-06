# withCString(encodedAs:_:)

**Framework**: Swift  
**Kind**: method

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
func withCString<Result, TargetEncoding>(encodedAs targetEncoding: TargetEncoding.Type, _ body: (UnsafePointer<TargetEncoding.CodeUnit>) throws -> Result) rethrows -> Result where TargetEncoding : _UnicodeEncoding
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(encodedAs:_:)`. Do not store or return the pointer for later use.

## Parameters

- `targetEncoding`: The encoding in which the code units should be   interpreted.
- `body`: A closure with a pointer parameter that points to a   null-terminated sequence of code units. If   has a return   value, that value is also used as the return value for the    method. The pointer argument is valid   only for the duration of the method’s execution.

## See Also

- [var utf8CString: ContiguousArray<CChar>](string/utf8cstring.md)
  A contiguously stored null-terminated UTF-8 representation of the string.
- [func withCString<Result>((UnsafePointer<Int8>) throws -> Result) rethrows -> Result](string/withcstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/withcstring(encodedas:_:))*