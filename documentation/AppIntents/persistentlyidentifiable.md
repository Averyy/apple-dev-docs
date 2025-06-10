# PersistentlyIdentifiable

**Framework**: App Intents  
**Kind**: protocol

Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol PersistentlyIdentifiable
```

## Topics

### Type Properties
- [static var persistentIdentifier: String](persistentlyidentifiable/persistentidentifier.md)
  A string that uniquely identifies this type.

## Relationships

### Inherited By
- [AppEntity](appentity.md)
- [AppEnum](appenum.md)
- [AppIntent](appintent.md)
- [AppValue](appvalue.md)
- [AssistantEntity](assistantentity.md)
- [AssistantEnum](assistantenum.md)
- [AssistantIntent](assistantintent.md)
- [AssistantSchemaEntity](assistantschemaentity.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [AssistantSchemaIntent](assistantschemaintent.md)
- [AudioPlaybackIntent](audioplaybackintent.md)
- [AudioRecordingIntent](audiorecordingintent.md)
- [AudioStartingIntent](audiostartingintent.md)
- [CameraCaptureIntent](cameracaptureintent.md)
- [ControlConfigurationIntent](controlconfigurationintent.md)
- [CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
- [DeleteIntent](deleteintent.md)
- [DeprecatedAppIntent](deprecatedappintent.md)
- [EntityPropertyQuery](entitypropertyquery.md)
- [EntityQuery](entityquery.md)
- [EntityStringQuery](entitystringquery.md)
- [EnumerableEntityQuery](enumerableentityquery.md)
- [FileEntity](fileentity.md)
- [ForegroundContinuableIntent](foregroundcontinuableintent.md)
- [IndexedEntity](indexedentity.md)
- [IntentValueQuery](intentvaluequery.md)
- [LiveActivityIntent](liveactivityintent.md)
- [LiveActivityStartingIntent](liveactivitystartingintent.md)
- [OpenIntent](openintent.md)
- [PauseWorkoutIntent](pauseworkoutintent.md)
- [PlayVideoIntent](playvideointent.md)
- [PredictableIntent](predictableintent.md)
- [ProgressReportingIntent](progressreportingintent.md)
- [PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
- [ResumeWorkoutIntent](resumeworkoutintent.md)
- [SetFocusFilterIntent](setfocusfilterintent.md)
- [SetValueIntent](setvalueintent.md)
- [ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
- [SnippetIntent](snippetintent.md)
- [StartDiveIntent](startdiveintent.md)
- [StartWorkoutIntent](startworkoutintent.md)
- [SystemIntent](systemintent.md)
- [TargetContentProvidingIntent](targetcontentprovidingintent.md)
- [TransientAppEntity](transientappentity.md)
- [UISceneAppIntent](uisceneappintent.md)
- [URLRepresentableEntity](urlrepresentableentity.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
- [URLRepresentableIntent](urlrepresentableintent.md)
- [UndoableIntent](undoableintent.md)
- [UniqueAppEntity](uniqueappentity.md)
- [UniqueAppEntityQuery](uniqueappentityquery.md)
- [WidgetConfigurationIntent](widgetconfigurationintent.md)
### Conforming Types
- [EmptySnippetIntent](emptysnippetintent.md)
- [OpenURLIntent](openurlintent.md)
- [StringSearchScope](stringsearchscope.md)
- [UniqueAppEntityProvider](uniqueappentityprovider.md)
- [VideoCategory](videocategory.md)

## See Also

- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/persistentlyidentifiable)*