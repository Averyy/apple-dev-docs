# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the observed object that creates bindings to its properties using dynamic member lookup.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

#### Discussion

Use the projected value to pass a binding value down a view hierarchy. To get the `projectedValue`, prefix the property variable with `$`.

## See Also

- [var wrappedValue: DelegateType](wkapplicationdelegateadaptor/wrappedvalue.md)
  The underlying delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue)*