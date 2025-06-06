# Never

**Framework**: Swift  
**Kind**: enum

A type that has no values and can’t be constructed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum Never
```

#### Overview

Use `Never` as the return type of a function that doesn’t return normally — for example, because it runs forever or terminates the program.

```swift
// An infinite loop never returns.
func forever() -> Never {
    while true {
        print("I will print forever.")
    }
}

// Calling fatalError(_:file:line:) unconditionally stops the program.
func crashAndBurn() -> Never {
    fatalError("Something very, very bad happened")
}
```

A function that returns `Never` is called a  function. Closures, methods, computed properties, and subscripts can also be nonreturning.

There’s no way to create an instance of `Never`; this characteristic makes it an  type. You can use an uninhabited type like `Never` to represent states in your program that are impossible to reach during execution. Swift’s type system uses this information — for example, to reason about control statements in cases that are known to be unreachable.

```swift
let favoriteNumber: Result<Int, Never> = .success(42)
switch favoriteNumber {
case .success(let value):
    print("My favorite number is", value)
}
```

In the code above, `favoriteNumber` has a failure type of `Never`, indicating that it always succeeds. The switch statement is therefore exhaustive, even though it doesn’t contain a `.failure` case, because that case could never be reached.

## Topics

### Type Aliases
- [typealias MapContentValue](never/mapcontentvalue.md)
- [typealias Specification](never/specification.md)
- [typealias UnwrappedType](never/unwrappedtype.md)
- [typealias ValueType](never/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<Never>](never/defaultresolverspecification.md)
### Default Implementations
- [AppIntent Implementations](never/appintent-implementations.md)
- [AtomicRepresentable Implementations](never/atomicrepresentable-implementations.md)
- [AttachmentContent Implementations](never/attachmentcontent-implementations.md)
- [Comparable Implementations](never/comparable-implementations.md)
- [Decodable Implementations](never/decodable-implementations.md)
- [Encodable Implementations](never/encodable-implementations.md)
- [Equatable Implementations](never/equatable-implementations.md)
- [Hashable Implementations](never/hashable-implementations.md)
- [Identifiable Implementations](never/identifiable-implementations.md)
- [IntentResult Implementations](never/intentresult-implementations.md)
- [ParameterSummary Implementations](never/parametersummary-implementations.md)
- [PersistentlyIdentifiable Implementations](never/persistentlyidentifiable-implementations.md)
- [TestScoping Implementations](never/testscoping-implementations.md)
- [TransferRepresentation Implementations](never/transferrepresentation-implementations.md)
- [Transferable Implementations](never/transferable-implementations.md)

## Relationships

### Conforms To
- [AccessibilityRotorContent](../SwiftUI/AccessibilityRotorContent.md)
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [AppIntent](../AppIntents/AppIntent.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [AttachmentContent](../RealityKit/AttachmentContent.md)
- [AxisContent](../Charts/AxisContent.md)
- [AxisMark](../Charts/AxisMark.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [ChartContent](../Charts/ChartContent.md)
- [Commands](../SwiftUI/Commands.md)
- [Comparable](comparable.md)
- [ControlWidgetConfiguration](../SwiftUI/ControlWidgetConfiguration.md)
- [ControlWidgetTemplate](../SwiftUI/ControlWidgetTemplate.md)
- [Copyable](copyable.md)
- [CustomHoverEffect](../SwiftUI/CustomHoverEffect.md)
- [CustomizableToolbarContent](../SwiftUI/CustomizableToolbarContent.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Error](error.md)
- [Gesture](../SwiftUI/Gesture.md)
- [Hashable](hashable.md)
- [Identifiable](identifiable.md)
- [ImmersiveSpaceContent](../SwiftUI/ImmersiveSpaceContent.md)
- [IntentResult](../AppIntents/IntentResult.md)
- [Keyframes](../SwiftUI/Keyframes.md)
- [MapContent](../MapKit/MapContent.md)
- [MapSelectable](../MapKit/MapSelectable.md)
- [ParameterSummary](../AppIntents/ParameterSummary.md)
- [PersistentlyIdentifiable](../AppIntents/PersistentlyIdentifiable.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [Scene](../SwiftUI/Scene.md)
- [Sendable](sendable.md)
- [ShapeStyle](../SwiftUI/ShapeStyle.md)
- [SortComparator](../Foundation/SortComparator.md)
- [StoreContent](../StoreKit/StoreContent.md)
- [TableColumnContent](../SwiftUI/TableColumnContent.md)
- [TableRowContent](../SwiftUI/TableRowContent.md)
- [TestScoping](../Testing/TestScoping.md)
- [ToolbarContent](../SwiftUI/ToolbarContent.md)
- [TransferRepresentation](../CoreTransferable/TransferRepresentation.md)
- [Transferable](../CoreTransferable/Transferable.md)
- [View](../SwiftUI/View.md)
- [WidgetConfiguration](../SwiftUI/WidgetConfiguration.md)

## See Also

- [func fatalError(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](fatalerror(_:file:line:).md)
  Unconditionally prints a given message and stops execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never)*