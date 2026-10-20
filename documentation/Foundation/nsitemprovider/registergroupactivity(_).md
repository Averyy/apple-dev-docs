# registerGroupActivity(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a group activity instance with the specificed options.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
func registerGroupActivity<ActivityType>(_ activity: ActivityType) where ActivityType : GroupActivity
```

## Parameters

- `activity`: The `GroupActivity` to register.

## See Also

### Registering group activities
- [func registerGroupActivity<ActivityType>(preparationHandler: () async throws -> ActivityType)](./registergroupactivity%28preparationhandler%29.md)
  Registers a group activity instance asynchronously with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registergroupactivity(_:))*