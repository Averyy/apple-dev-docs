# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Changes the name of the accessory.

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
- (void) updateName:(NSString *) name completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `name`: The new name.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Identifying an Accessory
- [var name: String](./name.md)
  The name of the accessory.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the accessory.
- [var identifier: UUID](./identifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/updatename(_:completionhandler:))*