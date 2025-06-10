# keySetReadAllIndices(withExpectedValues:expectedValueInterval:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func keySetReadAllIndices(withExpectedValues expectedValues: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func keySetReadAllIndices(withExpectedValues expectedValues: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroupkeymanagement/keysetreadallindices(withexpectedvalues:expectedvalueinterval:completion:))*