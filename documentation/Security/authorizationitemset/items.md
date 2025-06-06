# items

**Framework**: Security  
**Kind**: property

A pointer to an array of authorization items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var items: UnsafeMutablePointer<AuthorizationItem>?
```

#### Discussion

If `count` is greater than `1`, `items` points to the first item in an array of such items. You should set this parameter to `NULL` if there are no items.

Ensure that the array of items does not contain duplicates because it actually represents a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationitemset/items)*