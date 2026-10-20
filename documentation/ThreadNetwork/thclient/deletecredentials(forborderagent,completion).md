# deleteCredentials(forBorderAgent:completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Deletes Thread network credentials from the framework database for a Border Agent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func deleteCredentials(forBorderAgent borderAgentID: Data, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func deleteCredentials(forBorderAgent borderAgentID: Data) async throws
```

```objc
- (void) deleteCredentialsForBorderAgent:(NSData *) borderAgentID completion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Managing Thread network credentials](../managing-thread-network-credentials.md)

#### Discussion

> **Concurrency note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func deleteCredentials(forBorderAgent borderAgentID: Data) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The Border Agent is the software component running in the Thread Border Router responsible for advertising itself in the Wi-Fi or Ethernet network.

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

### Storing and Deleting Credentials
- [func storeCredentials(forBorderAgent: Data, activeOperationalDataSet: Data, completion: ((any Error)?) -> Void)](./storecredentials%28forborderagent,activeoperationaldataset,completion%29.md)
  Stores Thread network credentials into the framework database that a Border Agent provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/deletecredentials(forborderagent:completion:))*