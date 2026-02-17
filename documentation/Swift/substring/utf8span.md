# utf8Span

**Framework**: Swift  
**Kind**: property

A UTF-8 span over the code units that make up this substring.

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
var utf8Span: UTF8Span { get }
```

#### Return Value

A `UTF8Span` over the code units of this substring.

#### Discussion

> **Note**: In the case of bridged UTF-16 string instances (on Apple platforms) this property needs to transcode the code units every time it’s called.

For example, if `string` has the bridged UTF-16 representation, the following code is accidentally quadratic because of this issue:

```swift
for word in string.split(separator: " ") {
    useSpan(word.span)
}
```

A workaround is to explicitly convert the string into its native UTF-8 representation:

```swift
var nativeString = consume string
nativeString.makeContiguousUTF8()
for word in nativeString.split(separator: " ") {
    useSpan(word.span)
}
```

This second option has linear time complexity, as expected.

> **Note**: O(1) for native UTF-8 strings, O(n) for bridged UTF-16 strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf8span)*