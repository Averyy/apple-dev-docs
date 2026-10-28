# CFNotificationCenterGetLocalCenter()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the application’s local notification center.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFNotificationCenterGetLocalCenter() -> CFNotificationCenter!
```

```c
extern CFNotificationCenterRefCFNotificationCenterGetLocalCenter();
```

## Return Value

The application’s local notification center. An application has only one local notification center, so this function returns the same value each time it is called.

## See Also

### Accessing a Notification Center
- [func CFNotificationCenterGetDarwinNotifyCenter() -> CFNotificationCenter!](./cfnotificationcentergetdarwinnotifycenter%28%29.md)
  Returns the application’s Darwin notification center.
- [func CFNotificationCenterGetDistributedCenter() -> CFNotificationCenter!](./cfnotificationcentergetdistributedcenter%28%29.md)
  Returns the application’s distributed notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcentergetlocalcenter())*