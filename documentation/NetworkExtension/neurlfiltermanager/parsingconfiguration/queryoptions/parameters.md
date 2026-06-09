# parameters

**Framework**: Network Extension  
**Kind**: property

An array of parameter names to extract.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var parameters: [String]?
```

#### Discussion

Use a value of `nil` to include all query items.

If you specify an array for `parameters`, the parser includes the query items in the result, in the specified order.

For example, setting `parameters` to `["id", "external"]` parses URL `http://example.com/a/b/c?external&id=123&type=abc` into `http://example.com/a/b/c?id=123&external`. Note in this example that the query separates items with the `&` character, and query items don’t necessarily have a value (such as `external` in this example).

## See Also

- [var excluded: Bool](neurlfiltermanager/parsingconfiguration/queryoptions/excluded.md)
  A Boolean value that indicates whether to exclude the query component from URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/queryoptions/parameters)*