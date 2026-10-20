# getAnyDeviceController(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func getAnyDeviceController(completion: @escaping @Sendable (Any?, (any Error)?) -> Void)
```

```swift
func anyDeviceController() async throws -> Any
```

```objc
- (void) getAnyDeviceControllerWithCompletion:(MTRDeviceControllerGetterHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/getanydevicecontroller(completion:))*