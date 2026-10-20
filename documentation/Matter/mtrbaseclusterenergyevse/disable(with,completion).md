# disable(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command Disable

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
func disable(with params: MTREnergyEVSEClusterDisableParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func disable(with params: MTREnergyEVSEClusterDisableParams?) async throws
```

```objc
- (void) disableWithParams:(MTREnergyEVSEClusterDisableParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

Allows a client to disable the EVSE from charging and discharging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/disable(with:completion:))*