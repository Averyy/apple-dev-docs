---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/insertviewcontroller(_:at:animated:)"
framework: "CareKit/CareKit"
---

# insertViewController(_:at:animated:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Sets up the containment of `viewController` in OCKListViewController and inserts its view in the vertical stack of listed views at the specified index.

## Declaration

```swift
@MainActor
func insertViewController(_ viewController: UIViewController, at index: Int, animated: Bool)
```

## Parameters

- `viewController`: The view controller with the view to insert. If the view controller is already the child of a container view controller, it is removed from that container before being inserted.
- `index`: The index at which to insert the `viewController`’s view. This value must not be greater than the number of views in the `OCKListViewController`. If the index is out of bounds, this method throws an internalInconsistencyException exception.
- `animated`: Pass `true` to animate the insertion of `viewController`’s view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/insertviewcontroller(_:at:animated:))*