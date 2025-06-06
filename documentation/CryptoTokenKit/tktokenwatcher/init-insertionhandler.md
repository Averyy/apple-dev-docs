# init(insertionHandler:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a token watcher with the specified insertion handler.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(insertionHandler: @escaping (String) -> Void)
```

#### Return Value

A new token watcher object.

#### Discussion

This is the designated initializer.

## Parameters

- `insertionHandler`: A block to be called each time a token is added. This block takes a single argument:

## See Also

- [init()](tktokenwatcher/init.md)
  Initializes a token watcher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/init(insertionhandler:))*