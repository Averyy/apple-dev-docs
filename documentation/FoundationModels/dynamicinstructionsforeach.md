# DynamicInstructionsForEach

**Framework**: Foundation Models  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct DynamicInstructionsForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable, Content : DynamicInstructions
```

## Topics

### Creating an instance
- [init(Data, content: (Data.Element) -> Content)](dynamicinstructionsforeach/init(_:content:).md)
- [init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content)](dynamicinstructionsforeach/init(_:id:content:).md)

## Relationships

### Conforms To
- [DynamicInstructions](dynamicinstructions.md)

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsforeach)*