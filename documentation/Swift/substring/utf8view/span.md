# span

**Framework**: Swift  
**Kind**: property

A span over the UTF8 code units that make up this substring.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var span: Span<UTF8.CodeUnit> { get }
```

#### Discussion

> **Note**: In the case of bridged UTF16 String instances (on Apple platforms,) this property needs to transcode the code units every time it is called. For example, if `string` has the bridged UTF16 representation, for word in string.split(separator: “ “) { useSpan(word.span) } is accidentally quadratic because of this issue. A workaround is to explicitly convert the string into its native UTF8 representation: var nativeString = consume string nativeString.makeContiguousUTF8() for word in nativeString.split(separator: “ “) { useSpan(word.span) } This second option has linear time complexity, as expected.

Returns: a `Span` over the UTF8 code units of this Substring.

Complexity: O(1) for native UTF8 Strings, O(n) for bridged UTF16 Strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf8view/span)*