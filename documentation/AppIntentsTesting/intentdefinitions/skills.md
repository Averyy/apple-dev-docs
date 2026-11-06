# skills

**Framework**: App Intents Testing  
**Kind**: property  
**Role**: Instance Property

The definitions of the app’s skills, keyed by skill name.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var skills: IntentDefinitions.DefinitionCollection<SkillDefinition> { get }
```

## Discussion

```swift
let definitions = IntentDefinitions(bundleIdentifier: "com.apple.example")
let planTripSkill = definitions.skills["plan-trip"]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentdefinitions/skills)*