# SkillDefinition

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

A definition that identifies one of an app’s skills by the app’s bundle identifier and the skill’s name.

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
struct SkillDefinition
```

## Overview

Get a skill definition from the [`skills`](./intentdefinitions/skills.md) collection of the app’s [`IntentDefinitions`](./intentdefinitions.md):

```swift
let definitions = IntentDefinitions(bundleIdentifier: "com.apple.example")
let planTripSkill = definitions.skills["plan-trip"]
```

## Topics

### Instance Properties
- [let bundleIdentifier: String](./skilldefinition/bundleidentifier.md)
  The bundle identifier of the app that includes this skill.
- [let skillName: String](./skilldefinition/skillname.md)
  The skill’s name.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/skilldefinition)*