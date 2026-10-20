# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the name of the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateName(_ name: String, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateName(_ name: String) async throws
```

```objc
- (void) updateName:(NSString *) name completionHandler:(HMErrorBlock) completion;
```

## Parameters

- `name`: The new name; must not be `nil`.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Identifiying an action set
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The action set’s unique identifier.
- [var name: String](./name.md)
  The name of the action set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/updatename(_:completionhandler:))*