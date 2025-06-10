# values(forAttributes:forItemWith:completion:)

**Framework**: Finder Sync  
**Kind**: method

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func values(forAttributes attributes: [URLResourceKey], forItemWith itemURL: URL) async throws -> [URLResourceKey : Any]
```

#### Overview

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func values(forAttributes attributes: [URLResourceKey], forItemWith itemURL: URL) async throws -> [URLResourceKey : Any]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/values(forattributes:foritemwith:completion:))*