# local

**Framework**: App Intents  
**Kind**: property

The identifier you use to refer to the entity on the current device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let local: LocalID?
```

#### Discussion

Use this property to retrieve the local identifier value you specified at initialization time. When the framework performs entity resolution across devices, the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/local)*