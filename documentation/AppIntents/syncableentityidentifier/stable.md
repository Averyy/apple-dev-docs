# stable

**Framework**: App Intents  
**Kind**: property

The identifier you use to refer to the entity across devices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let stable: StableID?
```

#### Discussion

Use this property to retrieve the stable identifier value you specified at initialization time. When the framework creates identifiers for on-device operations, it can set this property to `nil` if it doesn’t need the stable identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/stable)*