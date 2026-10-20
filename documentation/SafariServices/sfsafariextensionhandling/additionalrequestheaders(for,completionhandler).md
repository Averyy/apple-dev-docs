# additionalRequestHeaders(for:completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.13.4+

## Declaration

```swift
optional func additionalRequestHeaders(for url: URL, completionHandler: @escaping @Sendable ([String : String]?) -> Void)
```

```swift
optional func additionalRequestHeaders(for url: URL) async -> [String : String]?
```

```objc
- (void) additionalRequestHeadersForURL:(NSURL *) url completionHandler:(void (^)(NSDictionary<NSString *,NSString *> *)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> optional func additionalRequestHeaders(for url: URL) async -> [String : String]?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/additionalrequestheaders(for:completionhandler:))*