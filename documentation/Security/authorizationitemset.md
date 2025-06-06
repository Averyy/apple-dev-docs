# AuthorizationItemSet

**Framework**: Security  
**Kind**: struct

A structure containing a set of authorization items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AuthorizationItemSet
```

#### Overview

Because it is actually a set, the list of items should not contain any duplicates.

## Topics

### Initializers
- [init()](authorizationitemset/init.md)
  Initializes an authorization item set.
- [init(count: UInt32, items: UnsafeMutablePointer<AuthorizationItem>?)](authorizationitemset/init(count:items:).md)
  Initializes an authorization item set with the given items.
### Instance Properties
- [var count: UInt32](authorizationitemset/count.md)
  The number of elements in the `items` array.
- [var items: UnsafeMutablePointer<AuthorizationItem>?](authorizationitemset/items.md)
  A pointer to an array of authorization items.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationitemset)*