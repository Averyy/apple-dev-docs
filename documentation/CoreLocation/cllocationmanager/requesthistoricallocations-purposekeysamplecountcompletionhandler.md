# requestHistoricalLocations(purposeKey:sampleCount:completionHandler:)

**Framework**: Core Location  
**Kind**: method

**Availability**:
- watchOS 9.0+

## Declaration

```swift
func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requesthistoricallocations(purposekey:samplecount:completionhandler:))*