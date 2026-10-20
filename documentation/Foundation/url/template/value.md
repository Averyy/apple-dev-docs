# URL.Template.Value

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The value of a variable used for expanding a template.

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
struct Value
```

#### Overview

A value can either be some text, a list, or an associate list (a dictionary).

##### Examples

```swift
let hello: URL.Template.Value = .text("Hello World!")
let list: URL.Template.Value = .list(["red", "green", "blue"])
let keys: URL.Template.Value = .associativeList([
    "semi": ";",
    "dot": ".",
    "comma": ",",
])
```

Alternatively, for constants, the `ExpressibleBy…Literal` implementations can be used, i.e.

```swift
let hello: URL.Template.Value = "Hello World!"
let list: URL.Template.Value = ["red", "green", "blue"]
let keys: URL.Template.Value = [
    "semi": ";",
    "dot": ".",
    "comma": ",",
]
```

## Topics

### Type Methods
- [static func associativeList(some Sequence<(key: String, value: String)>) -> URL.Template.Value](./value/associativelist%28_%29.md)
  An associative list value (ordered key-value pairs) to be used with a `URL.Template`.
- [static func list(some Sequence<String>) -> URL.Template.Value](./value/list%28_%29.md)
  A list value (an array of `String`s) to be used with a `URL.Template`.
- [static func text(String) -> URL.Template.Value](./value/text%28_%29.md)
  A text value to be used with a `URL.Template`.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [ExpressibleByDictionaryLiteral](../../../Swift/expressiblebydictionaryliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/template/value)*