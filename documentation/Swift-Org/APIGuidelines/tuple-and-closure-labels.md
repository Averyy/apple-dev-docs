---
url: "https://docs.swift.org/latest/documentation/apiguidelines/tuple-and-closure-labels"
framework: "Swift-Org/APIGuidelines"
---

# Label tuple members and name closure parameters

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Label tuple members and name closure parameters where they appear in your API.

## Overview

These names have explanatory power, can be referenced from documentation comments, and provide expressive access to tuple members.

```swift
/// Ensure that we hold uniquely-referenced storage for at least
/// `requestedCapacity` elements.
///
/// If more storage is needed, `allocate` is called with
/// **`byteCount`** equal to the number of maximally-aligned
/// bytes to allocate.
///
/// - Returns:
///   - **reallocated**: `true` if a new block of memory
///     was allocated; otherwise, `false`.
///   - **capacityChanged**: `true` if `capacity` was updated;
///     otherwise, `false`.
mutating func ensureUniqueStorage(
  minimumCapacity requestedCapacity: Int,
  allocate: (_ **byteCount**: Int) -> UnsafePointer<Void>
) -> (**reallocated:** Bool, **capacityChanged:** Bool)
```

Names used for closure parameters should be chosen like parameter names (see [Choose parameter names to serve documentation](./parameter-names-for-documentation.md)) for top-level functions. Labels for closure arguments that appear at the call site are not supported.

## See Also

### Special Instructions
- [Take extra care with unconstrained polymorphism](./unconstrained-polymorphism.md)
  Take extra care with unconstrained polymorphism to avoid ambiguities in overload sets.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/tuple-and-closure-labels)*