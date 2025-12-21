# IntentChoiceOption

**Framework**: App Intents  
**Kind**: struct

A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct IntentChoiceOption
```

#### Overview

Each option includes display text and an optional style that influences its visual presentation. For example, an option for deleting a file might use a text and style to communicate its destructive action.

## Topics

### Structures
- [IntentChoiceOption.Style](intentchoiceoption/style-swift.struct.md)
  Defines the visual style and semantic meaning of an [`IntentChoiceOption`](intentchoiceoption.md).
### Initializers
- [init(title: LocalizedStringResource, style: IntentChoiceOption.Style)](intentchoiceoption/init(title:style:).md)
  Creates a new option for a person to choose to continue an app intent.
### Instance Properties
- [let style: IntentChoiceOption.Style](intentchoiceoption/style-swift.property.md)
  The style applied to the option, affecting its visual appearance in the system UI.
- [let title: LocalizedStringResource](intentchoiceoption/title.md)
  The localized text displayed for this option.
### Type Properties
- [static var cancel: IntentChoiceOption](intentchoiceoption/cancel.md)
  A system-provided option that cancel the app intent.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption)*