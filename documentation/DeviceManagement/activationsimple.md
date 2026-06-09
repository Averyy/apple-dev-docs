# ActivationSimple

**Framework**: Device Management  
**Kind**: dictionary

The declaration to activate a set of configurations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ActivationSimple
```

#### Discussion

Specify `com.apple.activation.simple` as the declaration type.

##### Activation Examples

**One configuration**:

This activation applies one configuration.

```json
{
    "Type": "com.apple.activation.simple",
    "Identifier": "1A136E03-0979-4B79-BAE9-1A2A2A785D3F",
    "ServerToken": "F292FEF9-0C62-4E60-A989-2597352AA699",
    "Payload": {
        "StandardConfigurations": [
            "5D9502B9-9676-42D1-B094-A919DAFFB504"
        ]
    }
}
```

**Predicate**:

This activation applies two configurations and uses a predicate to limit those to only apply on an Apple TV device.

```json
{
    "Type": "com.apple.activation.simple",
    "Identifier": "04BECEFA-47B9-4F2E-8040-246509A52409",
    "ServerToken": "CBE396A0-637B-438D-9F0C-EA912A5BB587",
    "Payload": {
        "Predicate": "@status(device.model.family) == 'AppleTV'",
        "StandardConfigurations": [
            "892853C1-DDD1-4562-84B9-1591A76AD42B",
            "DCF869F1-09B7-4EC2-83B5-073F6FE94597"
        ]
    }
}
```

## Properties

- `Predicate` (string): A predicate format string as [`Apple’s Predicate Programming`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html) describes. The activation only installs when the predicate evaluates to `true` or isn’t present.
- `StandardConfigurations` ([string]) *(required)*: An array of strings that specify the identifiers of configurations to install. A failure to install one of the configurations doesn’t prevent other configurations from installing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activationsimple)*