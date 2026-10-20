# setCookingParametersWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetCookingParameters

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func setCookingParametersWith(_ params: MTRMicrowaveOvenControlClusterSetCookingParametersParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setCookingParametersWith(_ params: MTRMicrowaveOvenControlClusterSetCookingParametersParams?) async throws
```

```objc
- (void) setCookingParametersWithParams:(MTRMicrowaveOvenControlClusterSetCookingParametersParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is used to set the cooking parameters associated with the operation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovencontrol/setcookingparameterswith(_:completion:))*