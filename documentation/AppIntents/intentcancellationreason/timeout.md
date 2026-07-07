# timeout

**Framework**: App Intents  
**Kind**: property

An option that indicates the app intent exceeded the allowed time limit without reporting progress.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
static var timeout: IntentCancellationReason { get }
```

#### Discussion

When an app intent runs on iOS, iPadOS, tvOS, visionOS, or watchOS, it has a default timeout of around 30 seconds. If the app intent doesn’t report progress during this time, the system can cancel the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentcancellationreason/timeout)*