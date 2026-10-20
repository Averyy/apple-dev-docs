# init(insertionHandler:)

**Framework**: CryptoTokenKit  
**Kind**: init  
**Role**: Initializer

Initializes a token watcher with the specified insertion handler.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`init()`](./init%28%29.md) followed by a call to [`setInsertionHandler(_:)`](./setinsertionhandler%28_%29.md) instead.

## Declaration

```swift
init(insertionHandler: @escaping (String) -> Void)
```

```objc
- (instancetype) initWithInsertionHandler:(void (^)(NSString *tokenID)) insertionHandler;
```

#### Return Value

A new token watcher object.

#### Discussion

This is the designated initializer.

## Parameters

- `insertionHandler`: A block to be called each time a token is added. This block takes a single argument:

  - **tokenID**: The identifier of the added token.

## See Also

### Creating Token Watchers
- [init()](./init%28%29.md)
  Initializes a token watcher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/init(insertionhandler:))*