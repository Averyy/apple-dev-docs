# AssistantEntity(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app entity conforms to an assistant schema.

**Availability**:
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- iOS 16.0+

## Declaration

```swift
@attached
(memberAttribute) @attached(extension, conformances: AppEntity, AssistantSchemaEntity, names: named(__assistantSchemaEntity)) macro AssistantEntity<T>(schema: T) where T : AssistantSchemas.Entity
```

## Mentions

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
- [Making email actions available to Siri and Apple Intelligence](making-email-actions-available-to-siri-and-apple-intelligence.md)
- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)
- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)
- [Making spreadsheet actions available to Siri and Apple Intelligence](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md)
- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)
- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)
- [Making ebook actions available to Siri and Apple Intelligence](making-ebook-actions-available-to-siri-and-apple-intelligence.md)
- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)
- [Making file management actions available to Siri and Apple Intelligence](making-file-management-actions-available-to-siri-and-apple-intelligence.md)
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
- [Making journaling actions available to Siri and Apple Intelligence](making-journaling-actions-available-to-siri-and-apple-intelligence.md)

## See Also

- [macro AssistantIntent<T>(schema: T)](assistantintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an assistant schema.
- [macro AssistantEnum<T>(schema: T)](assistantenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to an assistant schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantentity(schema:))*