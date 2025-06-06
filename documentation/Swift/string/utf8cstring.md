# utf8CString

**Framework**: Swift  
**Kind**: property

A contiguously stored null-terminated UTF-8 representation of the string.

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
var utf8CString: ContiguousArray<CChar> { get }
```

#### Discussion

To access the underlying memory, invoke `withUnsafeBufferPointer` on the array.

```swift
let s = "Hello!"
let bytes = s.utf8CString
print(bytes)
// Prints "[72, 101, 108, 108, 111, 33, 0]"

bytes.withUnsafeBufferPointer { ptr in
    print(strlen(ptr.baseAddress!))
}
// Prints "6"
```

## See Also

- [func withCString<Result>((UnsafePointer<Int8>) throws -> Result) rethrows -> Result](string/withcstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws -> Result) rethrows -> Result](string/withcstring(encodedas:_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8cstring)*