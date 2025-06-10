# IntentParameterDependency

**Framework**: App Intents  
**Kind**: class

A property wrapper that represents an app intent dependency you use to provide dynamic options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@propertyWrapper
final class IntentParameterDependency<Intent> where Intent : AppIntent
```

#### Overview

Use the `IntentParameterDependency` property wrapper for properties that represent dynamic options in your [`DynamicOptionsProvider`](dynamicoptionsprovider.md) implementations as shown in the following example:

```swift
struct SoupQuery: EntityStringQuery {
    @IntentParameterDependency<OrderSoup>(
        \.$quantity
    )
    var orderSoup

    func entities(matching string: String) async throws -> [Soup] {
        guard let orderSoup else {
            return []
        }
        return Soup.allSoups.filter {
            $0.name.contains(string) &&
            $0.availableQuantity >= orderSoup.quantity
        }
    }
}
```

## Topics

### Initializers
- [convenience init<V0, P0>(KeyPath<Intent, P0>)](intentparameterdependency/init(_:).md)
- [convenience init<V0, P0, V1, P1>(KeyPath<Intent, P0>, KeyPath<Intent, P1>)](intentparameterdependency/init(_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>)](intentparameterdependency/init(_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>)](intentparameterdependency/init(_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>)](intentparameterdependency/init(_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>)](intentparameterdependency/init(_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>)](intentparameterdependency/init(_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9, V10, P10>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>, KeyPath<Intent, P10>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9, V10, P10, V11, P11>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>, KeyPath<Intent, P10>, KeyPath<Intent, P11>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9, V10, P10, V11, P11, V12, P12>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>, KeyPath<Intent, P10>, KeyPath<Intent, P11>, KeyPath<Intent, P12>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9, V10, P10, V11, P11, V12, P12, V13, P13>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>, KeyPath<Intent, P10>, KeyPath<Intent, P11>, KeyPath<Intent, P12>, KeyPath<Intent, P13>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4, V5, P5, V6, P6, V7, P7, V8, P8, V9, P9, V10, P10, V11, P11, V12, P12, V13, P13, V14, P14>(KeyPath<Intent, P0>, KeyPath<Intent, P1>, KeyPath<Intent, P2>, KeyPath<Intent, P3>, KeyPath<Intent, P4>, KeyPath<Intent, P5>, KeyPath<Intent, P6>, KeyPath<Intent, P7>, KeyPath<Intent, P8>, KeyPath<Intent, P9>, KeyPath<Intent, P10>, KeyPath<Intent, P11>, KeyPath<Intent, P12>, KeyPath<Intent, P13>, KeyPath<Intent, P14>)](intentparameterdependency/init(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
### Instance Properties
- [var wrappedValue: IntentProjection<Intent>?](intentparameterdependency/wrappedvalue.md)
### Default Implementations
- [CustomDebugStringConvertible Implementations](intentparameterdependency/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](intentparameterdependency/equatable-implementations.md)
- [Hashable Implementations](intentparameterdependency/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [struct IntentParameterContext](intentparametercontext.md)
  A type that provides information about an associated parameter during value resolution.
- [enum InputConnectionBehavior](inputconnectionbehavior.md)
  Describes the input behaviors for connecting a parameter to the output of the previous App Intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameterdependency)*