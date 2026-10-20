# Never

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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

A function that returns `Never` is called a *nonreturning* function. Closures, methods, computed properties, and subscripts can also be nonreturning.

There’s no way to create an instance of `Never`; this characteristic makes it an *uninhabited* type. You can use an uninhabited type like `Never` to represent states in your program that are impossible to reach during execution. Swift’s type system uses this information — for example, to reason about control statements in cases that are known to be unreachable.

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
- [typealias MapContentValue](./never/mapcontentvalue.md)
- [typealias Specification](./never/specification.md)
- [typealias UnwrappedType](./never/unwrappedtype.md)
- [typealias ValueType](./never/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<Never>](./never/defaultresolverspecification.md)
### Default Implementations
- [AtomicRepresentable Implementations](./never/atomicrepresentable-implementations.md)
- [Comparable Implementations](./never/comparable-implementations.md)
- [Decodable Implementations](./never/decodable-implementations.md)
- [Encodable Implementations](./never/encodable-implementations.md)
- [Equatable Implementations](./never/equatable-implementations.md)
- [Hashable Implementations](./never/hashable-implementations.md)
- [Identifiable Implementations](./never/identifiable-implementations.md)
- [TestScoping Implementations](./never/testscoping-implementations.md)

## Relationships

### Conforms To
- [AccessibilityRotorContent](../SwiftUI/accessibilityrotorcontent.md)
- [AppExtensionScene](../ExtensionKit/appextensionscene.md)
- [AppIntent](../AppIntents/appintent.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [AttachmentContent](../RealityKit/attachmentcontent.md)
- [AxisContent](../Charts/axiscontent.md)
- [AxisMark](../Charts/axismark.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [CMSampleBuffer.Content](../CoreMedia/cmsamplebuffer/content.md)
- [Chart3DContent](../Charts/chart3dcontent.md)
- [ChartContent](../Charts/chartcontent.md)
- [Commands](../SwiftUI/commands.md)
- [Comparable](./comparable.md)
- [CompositorContent](../SwiftUI/compositorcontent.md)
- [ControlWidgetConfiguration](../SwiftUI/controlwidgetconfiguration.md)
- [ControlWidgetTemplate](../SwiftUI/controlwidgettemplate.md)
- [ConvertibleFromGeneratedContent](../FoundationModels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/convertibletogeneratedcontent.md)
- [CoordinateSpace3D](../Spatial/coordinatespace3d.md)
- [CoordinateSpace3DFloat](../Spatial/coordinatespace3dfloat.md)
- [Copyable](./copyable.md)
- [CustomHoverEffect](../SwiftUI/customhovereffect.md)
- [CustomizableToolbarContent](../SwiftUI/customizabletoolbarcontent.md)
- [Decodable](./decodable.md)
- [DynamicInstructions](../FoundationModels/dynamicinstructions.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [Error](./error.md)
- [Escapable](./escapable.md)
- [Generable](../FoundationModels/generable.md)
- [Gesture](../SwiftUI/gesture.md)
- [Hashable](./hashable.md)
- [Identifiable](./identifiable.md)
- [ImmersiveSpaceContent](../SwiftUI/immersivespacecontent.md)
- [InstructionsRepresentable](../FoundationModels/instructionsrepresentable.md)
- [IntentResult](../AppIntents/intentresult.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [Keyframes](../SwiftUI/keyframes.md)
- [LanguageModelSession.DynamicProfile](../FoundationModels/languagemodelsession/dynamicprofile.md)
- [MapContent](../MapKit/mapcontent.md)
- [MapSelectable](../MapKit/mapselectable.md)
- [ParameterSummary](../AppIntents/parametersummary.md)
- [PersistentlyIdentifiable](../AppIntents/persistentlyidentifiable.md)
- [Plottable](../Charts/plottable.md)
- [PrimitivePlottableProtocol](../Charts/primitiveplottableprotocol.md)
- [PromptRepresentable](../FoundationModels/promptrepresentable.md)
- [ReportableMetadata](../StateReporting/reportablemetadata.md)
- [Scene](../SwiftUI/scene.md)
- [SceneAccessoryContent](../SwiftUI/sceneaccessorycontent.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [ShapeStyle](../SwiftUI/shapestyle.md)
- [SortComparator](../Foundation/sortcomparator.md)
- [StoreContent](../StoreKit/storecontent.md)
- [TableColumnContent](../SwiftUI/tablecolumncontent.md)
- [TableRowContent](../SwiftUI/tablerowcontent.md)
- [TestScoping](../Testing/testscoping.md)
- [ToolbarContent](../SwiftUI/toolbarcontent.md)
- [TransferRepresentation](../CoreTransferable/transferrepresentation.md)
- [Transferable](../CoreTransferable/transferable.md)
- [View](../SwiftUI/view.md)
- [WidgetConfiguration](../SwiftUI/widgetconfiguration.md)

## See Also

### Exiting a Program
- [func fatalError(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](./fatalerror%28_,file,line%29.md)
  Unconditionally prints a given message and stops execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never)*