# clearWebsiteData(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func clearWebsiteData(completionHandler completion: (@Sendable () -> Void)? = nil)
```

```swift
func clearWebsiteData() async
```

```objc
- (void) clearWebsiteDataWithCompletionHandler:(void (^)()) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func clearWebsiteData() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/datastore/clearwebsitedata(completionhandler:))*