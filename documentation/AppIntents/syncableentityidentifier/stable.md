# stable

**Framework**: App Intents  
**Kind**: property

The identifier you use to refer to the entity across devices.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
let stable: StableID?
```

#### Discussion

Use this property to retrieve the stable identifier value you specified at initialization time. When the framework creates identifiers for on-device operations, it can set this property to `nil` if it doesn’t need the stable identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/stable)*