# requestHistoricalLocations(purposeKey:sampleCount:completionHandler:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- watchOS 9.0+

## Declaration

```swift
func requestHistoricalLocations(purposeKey: String, sampleCount: Int, completionHandler handler: @escaping @Sendable ([CLLocation], (any Error)?) -> Void)
```

```swift
func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
```

```objc
- (void) requestHistoricalLocationsWithPurposeKey:(NSString *) purposeKey sampleCount:(NSInteger) sampleCount completionHandler:(void (^)(NSArray<CLLocation *> *, NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requesthistoricallocations(purposekey:samplecount:completionhandler:))*