# description(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a standard role description for a user interface element.

**Availability**:
- macOS

## Declaration

```swift
static func description(for element: Any) -> String?
```

```c
extern NSString *NSAccessibilityRoleDescriptionForUIElement(id element);
```

## Discussion

This function is like the [`description(with:)`](./description%28with%29.md) function, except that it queries `element` to get the role and subrole. The [`description(with:)`](./description%28with%29.md) function is more efficient, but this function is useful for accessorizing base classes so that they properly handle derived classes, which may override the subrole or even the role.

## See Also

### Descriptions
- [func description(with: NSAccessibility.Subrole?) -> String?](./description%28with%29.md)
  Returns a standard description for a role and subrole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/role/description(for:))*