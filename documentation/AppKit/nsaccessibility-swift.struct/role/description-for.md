# description(for:)

**Framework**: AppKit  
**Kind**: method

Returns a standard role description for a user interface element.

**Availability**:
- macOS ?+

## Declaration

```swift
static func description(for element: Any) -> String?
```

#### Discussion

This function is like the [`description(with:)`](nsaccessibility-swift.struct/role/description(with:).md) function, except that it queries `element` to get the role and subrole. The [`description(with:)`](nsaccessibility-swift.struct/role/description(with:).md) function is more efficient, but this function is useful for accessorizing base classes so that they properly handle derived classes, which may override the subrole or even the role.

## See Also

- [func description(with: NSAccessibility.Subrole?) -> String?](nsaccessibility-swift.struct/role/description(with:).md)
  Returns a standard description for a role and subrole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/role/description(for:))*