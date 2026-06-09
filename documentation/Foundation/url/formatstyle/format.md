# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a URL, using this style.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func format(_ value: URL) -> String
```

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple URL instances. The following example creates a custom format style and then uses it to format a variety of URLs in an array:

```swift
let style = URL.FormatStyle(
    scheme: .never,
    user: .never,
    password: .never,
    host: .omitSpecificSubdomains(["www", "mobile", "m."],
                                  includeMultiLevelSubdomains: true),
    port: .never,
    path: .always,
    query: .never,
    fragment: .never)
let urls = [
    URL(string: "https://www.example.com/path/one")!,
    URL(string: "https://beta.example.com/path/two")!,
    URL(string: "https://beta.staging.west.example.com/three")!,
    URL(string: "https://query.example.com/four?key4=value4")!
]
let formatted = urls.map { $0.formatted(style) } // ["example.com/path/one", "beta.example.com/path/two", "west.example.com/three", "query.example.com/four"]
```

To format a single floating-point value, use the [`URL`](url.md) instance method [`formatted(_:)`](url/formatted(_:).md) method passing in an instance of [`URL.FormatStyle`](url/formatstyle.md), or [`formatted()`](url/formatted().md) to use a default style.

## Parameters

- `value`: The URL to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/format(_:))*