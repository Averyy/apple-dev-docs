# canInit(with:)

**Framework**: Foundation  
**Kind**: method

Determines whether the protocol subclass can handle the specified request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func canInit(with request: URLRequest) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the protocol subclass can handle `request`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A subclass should inspect `request` and determine whether or not the implementation can perform a load with that request.

This is an abstract method and subclasses must provide an implementation.

## Parameters

- `request`: The request to be handled.

## See Also

- [class func canInit(with: URLSessionTask) -> Bool](urlprotocol/caninit(with:)-18gbo.md)
  Determines whether the protocol subclass can handle the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/caninit(with:)-76brg)*