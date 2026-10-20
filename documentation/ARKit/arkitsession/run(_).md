# run(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Runs a session with the data providers you supply.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
final func run(_ dataProviders: [any DataProvider]) async throws
```

#### Discussion

If you call this method without previously calling the [`requestAuthorization(for:)`](./requestauthorization%28for%29.md) method, and if any of the data providers you supply require authorization, the system prompts the user for authorization when you call [`run(_:)`](./run%28_%29.md). If you call this method on an already-running session, ARKit stops the previous providers unless they’re also in the new array of providers.

This method either throws an [`ARKitSession.Error`](./error.md) or asserts when there’s a problem with the data providers you supply. Potential problems include:

- Passing a data provider that’s already in use in another session
- Passing a data provider that’s stopped
- Passing a data provider that’s not supported in the current context, such as in Simulator

When this method throws an error, its session stops all of the associated data providers.

## Parameters

- `dataProviders`: The providers that supply data during this session.

## See Also

### Starting and stopping a session
- [convenience init()](./init%28%29.md)
  Creates a new session.
- [func stop()](./stop%28%29.md)
  Stops all data providers running in this session.
- [ARKitSession.Error](./error.md)
  An error that might occur when running data providers on an ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/run(_:))*