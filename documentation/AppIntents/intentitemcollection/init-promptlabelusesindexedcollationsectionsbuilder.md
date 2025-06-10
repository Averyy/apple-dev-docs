# init(promptLabel:usesIndexedCollation:sectionsBuilder:)

**Framework**: App Intents  
**Kind**: init

Create an `ItemCollection` containing `Items`, or one or more `Sections` provided by a builder.

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
init(promptLabel: LocalizedStringResource? = nil, usesIndexedCollation: Bool = false, @IntentItemSection<Result>.Builder sectionsBuilder: () -> [IntentItemSection<Result>])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitemcollection/init(promptlabel:usesindexedcollation:sectionsbuilder:))*