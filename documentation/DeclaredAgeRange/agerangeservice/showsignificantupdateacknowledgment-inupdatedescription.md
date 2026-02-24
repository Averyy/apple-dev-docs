# showSignificantUpdateAcknowledgment(in:updateDescription:)

**Framework**: Declared Age Range  
**Kind**: method

Displays a system-provided sheet for people to acknowledge a significant app update.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
@MainActor
func showSignificantUpdateAcknowledgment(in windowScene: UIWindowScene, updateDescription: String) async throws
```

#### Discussion

Call this function to inform people that your app has undergone a significant change that requires their acknowledgment.

> ❗ **Important**: Before calling this action, check `AgeRangeService/RegulatoryFeature/significantAppChangeAdult` to determine if a person is required to acknowledge your significant app change.

> **Note**: An error if the feature isn’t available or if the person isn’t an adult.

## Parameters

- `windowScene`: A window scene that will be used to present the acknowledgment sheet.
- `updateDescription`: A description of the significant update to show the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/showsignificantupdateacknowledgment(in:updatedescription:))*