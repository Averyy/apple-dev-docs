# formatted()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Formats the URL using a default format style.

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
func formatted() -> String
```

## Return Value

A string representation of the URL, formatted according to the default format style.

## Discussion

Use this method to create a string representation of a URL using the default [`URL.FormatStyle`](./formatstyle.md) configuration. As seen in the following example, the default style creates a string with the scheme, host, and path, but not the port or query.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted() // "https://www.example.com/path/to/endpoint"
```

To customize formatting of the URL, use [`formatted(_:)`](./formatted%28_%29.md), passing in a customized [`URL.FormatStyle`](./formatstyle.md).

## See Also

### Formatting a URL
- [func formatted<F>(F) -> F.FormatOutput](./formatted%28_%29.md)
  Formats the URL, using the provided format style.
- [struct FormatStyle](./formatstyle.md)
  A structure that converts between URL instances and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatted())*