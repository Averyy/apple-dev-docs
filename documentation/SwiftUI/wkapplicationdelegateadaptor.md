# WKApplicationDelegateAdaptor

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper that is used in `App` to provide a delegate from WatchKit.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency @propertyWrapper struct WKApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKApplicationDelegate
```

## Mentions

- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)

## Topics

### Creating a delegate adaptor
- [init(_:)](wkapplicationdelegateadaptor/init(_:).md)
  Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.
### Getting the delegate adaptor
- [var projectedValue: ObservedObject<DelegateType>.Wrapper](wkapplicationdelegateadaptor/projectedvalue.md)
  A projection of the observed object that creates bindings to its properties using dynamic member lookup.
- [var wrappedValue: DelegateType](wkapplicationdelegateadaptor/wrappedvalue.md)
  The underlying delegate.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md)
  A property wrapper type that you use to create a WatchKit extension delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor)*