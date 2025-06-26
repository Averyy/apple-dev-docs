# URL.Template.Value

**Framework**: Foundation  
**Kind**: struct

The value of a variable used for expanding a template.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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
- [static func associativeList(some Sequence<(key: String, value: String)>) -> URL.Template.Value](url/template/value/associativelist(_:).md)
  An associative list value (ordered key-value pairs) to be used with a `URL.Template`.
- [static func list(some Sequence<String>) -> URL.Template.Value](url/template/value/list(_:).md)
  A list value (an array of `String`s) to be used with a `URL.Template`.
- [static func text(String) -> URL.Template.Value](url/template/value/text(_:).md)
  A text value to be used with a `URL.Template`.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/template/value)*