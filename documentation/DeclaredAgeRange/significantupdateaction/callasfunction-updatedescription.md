# callAsFunction(updateDescription:)

**Framework**: Declared Age Range  
**Kind**: method

Shows the significant update acknowledgement interface.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
func callAsFunction(updateDescription: String) async throws
```

#### Discussion

Call this method when you need to inform people about significant changes to your app that require their acknowledgement and consent before proceeding. For a code example, refer to `EnvironmentValues/showSignificantUpdateAcknowledgement`.

> **Note**:  An error if the request fails.

## Parameters

- `updateDescription`: A clear description of what changed in your app and why acknowledgment is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/significantupdateaction/callasfunction(updatedescription:))*