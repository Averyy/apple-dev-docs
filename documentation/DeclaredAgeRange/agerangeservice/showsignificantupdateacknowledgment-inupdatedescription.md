# showSignificantUpdateAcknowledgment(in:updateDescription:)

**Framework**: Declared Age Range  
**Kind**: method

Displays a system-provided interface for people to acknowledge a significant app update.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
func showSignificantUpdateAcknowledgment(in windowScene: UIWindowScene, updateDescription: String) async throws
```

#### Discussion

Call this function to inform people that your app has undergone a significant change that requires their acknowledgment. For more information on what constitutes a significant app change, refer to [`SignificantAppUpdateTopic`](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic).

> ❗ **Important**: Before calling this function, check [`AgeRangeService.RegulatoryFeature`](agerangeservice/regulatoryfeature.md) to determine if a person must acknowledge your significant app change.

> **Note**: An error if the feature isn’t available.

## Parameters

- `windowScene`: A window scene that presents the acknowledgment interface.
- `updateDescription`: A clear description of what changed in your app and why acknowledgment is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/showsignificantupdateacknowledgment(in:updatedescription:))*