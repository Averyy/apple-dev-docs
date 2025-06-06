# deleteCredentials(forBorderAgent:completion:)

**Framework**: ThreadNetwork  
**Kind**: method

Deletes Thread network credentials from the framework database for a Border Agent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func deleteCredentials(forBorderAgent borderAgentID: Data) async throws
```

## Mentions

- [Managing Thread network credentials](managing-thread-network-credentials.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func deleteCredentials(forBorderAgent borderAgentID: Data) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func deleteCredentials(forBorderAgent borderAgentID: Data) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The Border Agent is the software component running in the Border Router responsible for advertising itself in the Wi-Fi or Ethernet network.

Call the method as follows:

```swift
func removeCredentials(borderAgentID: Data) async -> (Error?) {
    let client = THClient()
    var err:Error?
    do {
        err = try await client.deleteCredentials(forBorderAgent: borderAgentID) as? Error
    } catch {
        err = error
    }
    return (err)
}
```

## Parameters

- `borderAgentID`: The identifer of a Thread network Border Agent.
- `completion`: The completion handler the framework calls after deleting the credentials.

## See Also

- [func storeCredentials(forBorderAgent: Data, activeOperationalDataSet: Data, completion: ((any Error)?) -> Void)](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md)
  Stores Thread network credentials into the framework database that a Border Agent provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/deletecredentials(forborderagent:completion:))*