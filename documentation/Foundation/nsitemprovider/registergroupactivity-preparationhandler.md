# registerGroupActivity(preparationHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a group activity instance asynchronously with the specified options.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
func registerGroupActivity<ActivityType>(preparationHandler: @escaping () async throws -> ActivityType) where ActivityType : GroupActivity
```

## Parameters

- `preparationHandler`: The handler the service invokes when it registers the  .

## See Also

- [func registerGroupActivity<ActivityType>(ActivityType)](nsitemprovider/registergroupactivity(_:).md)
  Registers a group activity instance with the specificed options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registergroupactivity(preparationhandler:))*