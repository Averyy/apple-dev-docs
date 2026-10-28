# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a download task.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Please use -[NSURLSession downloadTaskWithRequest:] or other NSURLSession methods to create instances

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Discussion

Don’t use this initalizer to manually create download tasks. Instead, use the factory methods on [`URLSession`](../urlsession.md) to add tasks to an existing URL session.

## See Also

### Creating download tasks
- [class func new() -> Self](./new%28%29.md)
  Creates and initializes a download task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloadtask/init())*