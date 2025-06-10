# fetchData(forBundleIdentifier:itemIdentifier:contentType:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Fetches data from an external provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func fetchData(forBundleIdentifier bundleIdentifier: String, itemIdentifier: String, contentType: UTType) async throws -> Data
```

#### Discussion

Clients with the appropriate entitlements can use this method to fetch data from an external app such as Mail.

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func fetchData(forBundleIdentifier bundleIdentifier: String, itemIdentifier: String, contentType: UTType) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `bundleIdentifier`: The bundle identifier of the app to search.
- `itemIdentifier`: The app-specific identifier of the item you want.
- `contentType`: The type of data to fetch.
- `completionHandler`: The block to execute with the results. The block   has no return value and takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/fetchdata(forbundleidentifier:itemidentifier:contenttype:completionhandler:))*