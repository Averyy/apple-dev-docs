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
- [typealias MapContentValue](never/mapcontentvalue.md)
- [typealias Specification](never/specification.md)
- [typealias UnwrappedType](never/unwrappedtype.md)
- [typealias ValueType](never/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<Never>](never/defaultresolverspecification.md)
### Default Implementations
- [AtomicRepresentable Implementations](never/atomicrepresentable-implementations.md)
- [Comparable Implementations](never/comparable-implementations.md)
- [Decodable Implementations](never/decodable-implementations.md)
- [Encodable Implementations](never/encodable-implementations.md)
- [Equatable Implementations](never/equatable-implementations.md)
- [Hashable Implementations](never/hashable-implementations.md)
- [Identifiable Implementations](never/identifiable-implementations.md)
- [TestScoping Implementations](never/testscoping-implementations.md)

## Relationships

### Conforms To
- [AccessibilityRotorContent](../swiftui/accessibilityrotorcontent.md)
- [AppExtensionScene](../extensionkit/appextensionscene.md)
- [AppIntent](../appintents/appintent.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [AttachmentContent](../realitykit/attachmentcontent.md)
- [AxisContent](../charts/axiscontent.md)
- [AxisMark](../charts/axismark.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CMSampleBuffer.Content](../coremedia/cmsamplebuffer/content.md)
- [Chart3DContent](../charts/chart3dcontent.md)
- [ChartContent](../charts/chartcontent.md)
- [Commands](../swiftui/commands.md)
- [Comparable](comparable.md)
- [CompositorContent](../swiftui/compositorcontent.md)
- [ControlWidgetConfiguration](../swiftui/controlwidgetconfiguration.md)
- [ControlWidgetTemplate](../swiftui/controlwidgettemplate.md)
- [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md)
- [CoordinateSpace3D](../spatial/coordinatespace3d.md)
- [CoordinateSpace3DFloat](../spatial/coordinatespace3dfloat.md)
- [Copyable](copyable.md)
- [CustomHoverEffect](../swiftui/customhovereffect.md)
- [CustomizableToolbarContent](../swiftui/customizabletoolbarcontent.md)
- [Decodable](decodable.md)
- [DynamicInstructions](../foundationmodels/dynamicinstructions.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Error](error.md)
- [Escapable](escapable.md)
- [Generable](../foundationmodels/generable.md)
- [Gesture](../swiftui/gesture.md)
- [Hashable](hashable.md)
- [Identifiable](identifiable.md)
- [ImmersiveSpaceContent](../swiftui/immersivespacecontent.md)
- [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md)
- [IntentResult](../appintents/intentresult.md)
- [IntentValueConvertible](../appintents/intentvalueconvertible.md)
- [IntentValueExpressing](../appintents/intentvalueexpressing.md)
- [Keyframes](../swiftui/keyframes.md)
- [LanguageModelSession.DynamicProfile](../foundationmodels/languagemodelsession/dynamicprofile.md)
- [MapContent](../mapkit/mapcontent.md)
- [MapSelectable](../mapkit/mapselectable.md)
- [ParameterSummary](../appintents/parametersummary.md)
- [PersistentlyIdentifiable](../appintents/persistentlyidentifiable.md)
- [Plottable](../charts/plottable.md)
- [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md)
- [PromptRepresentable](../foundationmodels/promptrepresentable.md)
- [ReportableMetadata](../statereporting/reportablemetadata.md)
- [Scene](../swiftui/scene.md)
- [SceneAccessoryContent](../swiftui/sceneaccessorycontent.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [ShapeStyle](../swiftui/shapestyle.md)
- [SortComparator](../foundation/sortcomparator.md)
- [StoreContent](../storekit/storecontent.md)
- [TableColumnContent](../swiftui/tablecolumncontent.md)
- [TableRowContent](../swiftui/tablerowcontent.md)
- [TestScoping](../testing/testscoping.md)
- [ToolbarContent](../swiftui/toolbarcontent.md)
- [TransferRepresentation](../coretransferable/transferrepresentation.md)
- [Transferable](../coretransferable/transferable.md)
- [View](../swiftui/view.md)
- [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## See Also

- [func fatalError(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](fatalerror(_:file:line:).md)
  Unconditionally prints a given message and stops execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never)*