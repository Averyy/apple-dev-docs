# wrappedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The underlying delegate.

**Availability**:
- watchOS 7.0+ - Deprecated in 9.2

> **Deprecated**: Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

## Declaration

```swift
@MainActor
@preconcurrency var wrappedValue: DelegateType { get }
```

## See Also

### Getting the delegate adaptor
- [var projectedValue: ObservedObject<DelegateType>.Wrapper](./projectedvalue.md)
  A projection of the observed object that provides bindings to its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/wrappedvalue)*