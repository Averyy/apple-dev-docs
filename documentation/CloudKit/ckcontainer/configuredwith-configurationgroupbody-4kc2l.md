# configuredWith(configuration:group:body:)

**Framework**: CloudKit  
**Kind**: method

Applies a temporary configuration to the container within the scope of a closure that supports concurrency.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
@discardableResult
@preconcurrency func configuredWith<R>(configuration: CKOperation.Configuration? = nil, group: CKOperationGroup? = nil, body: @Sendable (CKContainer) async throws -> R) async rethrows -> R
```

#### Discussion

Use this method to apply a specific configuration to the current container that lasts only for the duration of the trailing closure. For example, you might want to temporarily elevate the quality of service (QoS) for a group of method calls, or allow one or more expensive method calls to execute only while the device is using WiFi.

```swift
func fetchShareParticipants(
    with phoneNumbers: [String]
) async throws -> [String : Result<CKShare.Participant, any Error>] {

    // Get a reference to the app's container.
    let container = CKContainer.default()

    // Create a configuration that denies cellular access.
    let config = CKOperation.Configuration()
    config.allowsCellularAccess = false

    // Configure the container and execute an expensive fetch.
    return try await container.configuredWith(configuration: config) { container in
        try await container.shareParticipants(forPhoneNumbers: phoneNumbers)
    }
}
```

## Parameters

- `configuration`: An interim configuration to apply to the current container.
- `group`: The group to associate with the methods you execute in the closure. Specifying a group helps the system prioritize those method calls, and helps you identify the calls in the server logs in CloudKit Console. For more information, see  .
- `body`: The closure to execute with the temporarily configured container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/configuredwith(configuration:group:body:)-4kc2l)*