# projectedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A projection of the observed object that creates bindings to its properties using dynamic member lookup.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to `ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

#### Discussion

Use the projected value to pass a binding value down a view hierarchy. To get the `projectedValue`, prefix the property variable with `$`.

## See Also

### Getting the delegate adaptor
- [var wrappedValue: DelegateType](./wrappedvalue.md)
  The underlying delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue)*