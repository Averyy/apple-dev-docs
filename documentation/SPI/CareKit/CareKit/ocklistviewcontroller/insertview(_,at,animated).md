---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/insertview(_:at:animated:)"
framework: "CareKit/CareKit"
---

# insertView(_:at:animated:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inserts a view in the vertical stack of listed views at the specified index.

## Declaration

```swift
@MainActor
func insertView(_ view: UIView, at index: Int, animated: Bool)
```

## Parameters

- `view`: The view to insert in the list.
- `index`: The index at which to insert `view`. This value must not be greater than the number of views in the `OCKListViewController`. If the index is out of bounds, this method throws an internalInconsistencyException exception.
- `animated`: Pass `true` to animate the insertion of `view`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/insertview(_:at:animated:))*