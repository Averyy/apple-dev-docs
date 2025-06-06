# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Formats the URL, using the provided format style.

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
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == URL
```

#### Return Value

A formatted string representation of the URL.

#### Discussion

Use this method when you want to format a single URL value with a specific format style, or call it repeatedly with different format styles. The following example uses the static accessor [`url`](formatstyle/url.md) to get a default style, then modifies its behavior to include or omit different URL components when [`formatted(_:)`](url/formatted(_:).md) creates the string:

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted(.url
    .scheme(.never)
    .host(.always)
    .port(.never)
    .path(.always)
    .query(.never)) // "www.example.com/path/to/endpoint"

```

## Parameters

- `format`: The format style to apply when formatting the URL.

## See Also

- [func formatted() -> String](url/formatted.md)
  Formats the URL using a default format style.
- [struct FormatStyle](url/formatstyle.md)
  A structure that converts between URL instances and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatted(_:))*