# new()

**Framework**: Foundation  
**Kind**: method

Creates and initializes a download task.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func new() -> Self
```

#### Discussion

Don’t use this method to manually create download tasks. Instead, use the factory methods on [`URLSession`](urlsession.md) to add tasks to an existing URL session.

## See Also

- [init()](urlsessiondownloadtask/init.md)
  Initializes a download task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloadtask/new())*