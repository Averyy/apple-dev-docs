# updates

**Framework**: PermissionKit  
**Kind**: property

Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never> { get }
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## See Also

- [static let current: CommunicationLimits](communicationlimits/current.md)
  The singleton app instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/updates)*