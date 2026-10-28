# setActivePresetRequestWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetActivePresetRequest

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
func setActivePresetRequestWith(_ params: MTRThermostatClusterSetActivePresetRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setActivePresetRequestWith(_ params: MTRThermostatClusterSetActivePresetRequestParams) async throws
```

```objc
- (void) setActivePresetRequestWithParams:(MTRThermostatClusterSetActivePresetRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command will set the active preset to the provided preset handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostat/setactivepresetrequestwith(_:completion:))*