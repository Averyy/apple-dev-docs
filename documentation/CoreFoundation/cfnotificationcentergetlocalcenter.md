# CFNotificationCenterGetLocalCenter()

**Framework**: Core Foundation  
**Kind**: func

Returns the application’s local notification center.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFNotificationCenterGetLocalCenter() -> CFNotificationCenter!
```

#### Return Value

The application’s local notification center. An application has only one local notification center, so this function returns the same value each time it is called.

## See Also

- [func CFNotificationCenterGetDarwinNotifyCenter() -> CFNotificationCenter!](cfnotificationcentergetdarwinnotifycenter().md)
  Returns the application’s Darwin notification center.
- [func CFNotificationCenterGetDistributedCenter() -> CFNotificationCenter!](cfnotificationcentergetdistributedcenter().md)
  Returns the application’s distributed notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcentergetlocalcenter())*