# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the name of the zone.

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

- `name`: The new name. Must not be `nil`; must be unique within the home.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Identifying a Zone
- [var name: String](./name.md)
  The name of the zone.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The unique identifier for a zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/updatename(_:completionhandler:))*