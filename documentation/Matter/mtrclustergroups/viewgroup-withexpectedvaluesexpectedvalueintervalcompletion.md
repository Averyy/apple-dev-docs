# viewGroup(with:expectedValues:expectedValueInterval:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func viewGroup(with params: MTRGroupsClusterViewGroupParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRGroupsClusterViewGroupResponseParams
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func viewGroup(with params: MTRGroupsClusterViewGroupParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRGroupsClusterViewGroupResponseParams
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroups/viewgroup(with:expectedvalues:expectedvalueinterval:completion:))*