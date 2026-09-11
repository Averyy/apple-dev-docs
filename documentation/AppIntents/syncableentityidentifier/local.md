# local

**Framework**: App Intents  
**Kind**: property

The identifier you use to refer to the entity on the current device.

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
let local: LocalID?
```

#### Discussion

Use this property to retrieve the local identifier value you specified at initialization time. When the framework performs entity resolution across devices, the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/local)*