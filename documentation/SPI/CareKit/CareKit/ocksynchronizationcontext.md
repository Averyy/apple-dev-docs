---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocksynchronizationcontext"
framework: "CareKit/CareKit"
---

# OCKSynchronizationContext

**Framework**: CareKit/CareKit  
**Kind**: struct  
**Role**: Structure

A data structure that provides context for a view model value.

## Declaration

```swift
struct OCKSynchronizationContext<ViewModel>
```

## Topics

### Initializers
- [init(viewModel: ViewModel, oldViewModel: ViewModel, animated: Bool)](./ocksynchronizationcontext/init%28viewmodel,oldviewmodel,animated%29.md)
### Instance Properties
- [let animated: Bool](./ocksynchronizationcontext/animated.md)
  A Boolean value that indicates the view model is animated.
- [let oldViewModel: ViewModel](./ocksynchronizationcontext/oldviewmodel.md)
  The previous view model value.
- [let viewModel: ViewModel](./ocksynchronizationcontext/viewmodel.md)
  The current view model value.
### Default Implementations
- [Equatable Implementations](./ocksynchronizationcontext/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Equatable
- Swift.Escapable

## See Also

### Displaying synchronized care data in UIKit
- [protocol ViewSynchronizing](./viewsynchronizing.md)
  A protocol that creates and updates a view.
- [class SynchronizedViewController](./synchronizedviewcontroller.md)
  A view controller that updates a view using a stream of data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocksynchronizationcontext)*