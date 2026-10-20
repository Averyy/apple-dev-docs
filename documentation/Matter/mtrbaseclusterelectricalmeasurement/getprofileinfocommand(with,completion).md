# getProfileInfoCommand(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+ - Deprecated in 18.2
- iPadOS 16.4+ - Deprecated in 18.2
- Mac Catalyst 16.4+ - Deprecated in 18.2
- macOS 13.3+ - Deprecated in 15.2
- tvOS 16.4+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.4+ - Deprecated in 11.2

> **Deprecated**: This command is deprecated

## Declaration

```swift
func getProfileInfoCommand(with params: MTRElectricalMeasurementClusterGetProfileInfoCommandParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func profileInfoCommand(with params: MTRElectricalMeasurementClusterGetProfileInfoCommandParams?) async throws
```

```objc
- (void) getProfileInfoCommandWithParams:(MTRElectricalMeasurementClusterGetProfileInfoCommandParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalmeasurement/getprofileinfocommand(with:completion:))*