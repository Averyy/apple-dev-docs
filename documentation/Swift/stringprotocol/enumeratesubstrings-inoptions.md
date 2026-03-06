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
- `opts`: Options specifying types of substrings and enumeration styles. If `opts` is omitted or empty, `body` is called a single time with the range of the string specified by `range`.
- `body`: The closure executed for each substring in the enumeration. The closure takes four arguments: - The enumerated substring. If `substringNotRequired` is included in `opts`, this parameter is `nil` for every execution of the closure.
- The range of the enumerated substring in the string that `enumerate(in:options:_:)` was called on.
- The range that includes the substring as well as any separator or filler characters that follow. For instance, for lines, `enclosingRange` contains the line terminators. The enclosing range for the first string enumerated also contains any characters that occur before the string. Consecutive enclosing ranges are guaranteed not to overlap, and every single character in the enumerated range is included in one and only one enclosing range.
- An `inout` Boolean value that the closure can use to stop the enumeration by setting `stop = true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/enumeratesubstrings(in:options:_:))*