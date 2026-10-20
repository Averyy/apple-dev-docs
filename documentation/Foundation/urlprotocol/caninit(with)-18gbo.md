# canInit(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Determines whether the protocol subclass can handle the specified task.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func canInit(with task: URLSessionTask) -> Bool
```

```objc
+ (BOOL) canInitWithTask:(NSURLSessionTask *) task;
```

#### Discussion

A subclass should inspect the task’s request and determine whether or not the implementation can perform a load with that task.

This is an abstract method and subclasses must provide an implementation.

## Parameters

- `task`: A URL session task containing the request to be handled.

## See Also

### Determining If a subclass can handle a request
- [class func canInit(with: URLRequest) -> Bool](./caninit%28with%29-76brg.md)
  Determines whether the protocol subclass can handle the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/caninit(with:)-18gbo)*