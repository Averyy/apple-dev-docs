# handleApplyUpdateRequest(forNodeID:controller:params:completionHandler:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
optional func handleApplyUpdateRequest(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams) async throws -> MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func handleApplyUpdateRequest(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams) async throws -> MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func handleApplyUpdateRequest(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams) async throws -> MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handleapplyupdaterequest(fornodeid:controller:params:completionhandler:))*