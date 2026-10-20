# getService(named:for:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func getService(named serviceName: NSFileProviderServiceName, for itemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping @Sendable (NSFileProviderService?, (any Error)?) -> Void)
```

```swift
func service(named serviceName: NSFileProviderServiceName, for itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderService?
```

```objc
- (void) getServiceWithName:(NSFileProviderServiceName) serviceName itemIdentifier:(NSFileProviderItemIdentifier) itemIdentifier completionHandler:(void (^)(NSFileProviderService *, NSError *)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func service(named serviceName: NSFileProviderServiceName, for itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderService?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/getservice(named:for:completionhandler:))*