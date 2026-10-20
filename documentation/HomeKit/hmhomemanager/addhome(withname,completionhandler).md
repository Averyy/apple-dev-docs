# addHome(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a new home to this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addHome(withName homeName: String, completionHandler completion: @escaping @Sendable (HMHome?, (any Error)?) -> Void)
```

```swift
func addHome(named homeName: String) async throws -> HMHome
```

```objc
- (void) addHomeWithName:(NSString *) homeName completionHandler:(void (^)(HMHome *home, NSError *error)) completion;
```

## Parameters

- `homeName`: The name of the new home. Must not match the name of an existing home.
- `completion`: The block executed after the request is processed.

  - **home**: The newly created home; may be `nil` if creation failed.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Adding and removing homes
- [func removeHome(HMHome, completionHandler: ((any Error)?) -> Void)](./removehome%28_,completionhandler%29.md)
  Removes a home from this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/addhome(withname:completionhandler:))*