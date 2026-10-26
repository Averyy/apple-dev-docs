---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/appendviewcontroller(_:animated:)"
framework: "CareKit/CareKit"
---

# appendViewController(_:animated:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Sets up the containment of `viewController` in OCKListViewController and appends its view to the vertical stack of listed views.

## Declaration

```swift
@MainActor
func appendViewController(_ viewController: UIViewController, animated: Bool)
```

## Parameters

- `viewController`: The view controller with the view to append. If the new child view controller is already the child of a container view controller, it is removed from that container before being appended..
- `animated`: Pass `true` to animate the addition of the `viewController`’s view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller/appendviewcontroller(_:animated:))*