# description(with:)

**Framework**: AppKit  
**Kind**: method

Returns a standard description for a role and subrole.

**Availability**:
- macOS ?+

## Declaration

```swift
func description(with subrole: NSAccessibility.Subrole?) -> String?
```

#### Discussion

You should pass `nil` to this function if there is no subrole. This function returns a description of a standard role. For example, if you implement a button widget that does not inherit from [`NSButton`](nsbutton.md), you should use this function to return a localized role description matching that returned by a standard button.

## See Also

- [static func description(for: Any) -> String?](nsaccessibility-swift.struct/role/description(for:).md)
  Returns a standard role description for a user interface element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/role/description(with:))*