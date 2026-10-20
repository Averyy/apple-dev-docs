# wrappedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The underlying app delegate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/wrappedvalue)*