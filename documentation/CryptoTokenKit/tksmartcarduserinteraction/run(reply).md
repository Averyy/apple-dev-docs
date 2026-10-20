# run(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Runs the user interaction and asynchronously receives a reply.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func run(reply: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func run() async throws -> Bool
```

```objc
- (void) runWithReply:(void (^)(BOOL success, NSError *error)) reply;
```

## Parameters

- `reply`:

  - **success**: Whether the user interaction was successful.
  - **error**: Contains information about the the error that occurred during the user interaction.

  The `NSError` object is created in the [`TKErrorDomain`](../tkerrordomain.md) domain with a code in the [`TKError.Code`](../tkerror/code.md) enumeration.

## See Also

### Starting and Stopping
- [func cancel() -> Bool](./cancel%28%29.md)
  Attempts to cancel an interaction started by calling [`run(reply:)`](./run%28reply%29.md). For certain interactions, cancellation may not be available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/run(reply:))*