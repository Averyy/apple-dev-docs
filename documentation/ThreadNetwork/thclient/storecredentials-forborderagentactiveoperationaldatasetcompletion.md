# storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)

**Framework**: ThreadNetwork  
**Kind**: method

Stores Thread network credentials into the framework database that a Border Agent provides.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func storeCredentials(forBorderAgent borderAgentID: Data, activeOperationalDataSet: Data) async throws
```

## Mentions

- [Managing Thread network credentials](managing-thread-network-credentials.md)
- [Configuring a Border Router](configuring-a-border-router.md)

#### Discussion

> ❗ **Important**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func storeCredentials(forBorderAgent borderAgentID: Data, activeOperationalDataSet: Data) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The Border Agent is the software component running in the Thread Border Router responsible for advertising itself in the Wi-Fi or Ethernet network.

The framework only stores credentials if it can find an mDNS record for the Border Agent that contains the specified Border Agent identifier.

Call the method as follows:

```swift
func saveCredentials(borderAgentID: Data, activeOperationalDataSet: Data) async -> (Error?) {
    let client = THClient()
    var err:Error?
    do {
        err = try await client.storeCredentials(forBorderAgent: borderAgentID, activeOperationalDataSet: activeOperationalDataSet) as? Error
    } catch {
        err = error
    }
    return (err)
}
```

## Parameters

- `borderAgentID`: The identifer of an active Thread network Border Agent.
- `activeOperationalDataSet`: The essential operational parameters for the Thread network.
- `completion`: The completion handler the framework calls after storing the credentials.

## See Also

- [func deleteCredentials(forBorderAgent: Data, completion: ((any Error)?) -> Void)](thclient/deletecredentials(forborderagent:completion:).md)
  Deletes Thread network credentials from the framework database for a Border Agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/storecredentials(forborderagent:activeoperationaldataset:completion:))*