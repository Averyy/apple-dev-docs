# enumerateSubstrings(in:options:_:)

**Framework**: Swift  
**Kind**: method

Enumerates the substrings of the specified type in the specified range of the string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateSubstrings<R>(in range: R, options opts: String.EnumerationOptions = [], _ body: @escaping (String?, Range<Self.Index>, Range<Self.Index>, inout Bool) -> Void) where R : RangeExpression, R.Bound == String.Index
```

#### Discussion

Mutation of a string value while enumerating its substrings is not supported. If you need to mutate a string from within `body`, convert your string to an `NSMutableString` instance and then call the `enumerateSubstrings(in:options:using:)` method.

## Parameters

- `range`: The range within the string to enumerate substrings.
- `opts`: Options specifying types of substrings and enumeration styles.   If   is omitted or empty,   is called a single time with   the range of the string specified by  .
- `body`: The closure executed for each substring in the enumeration. The   closure takes four arguments:


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/enumeratesubstrings(in:options:_:))*