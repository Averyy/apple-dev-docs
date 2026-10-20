# CFNotificationName

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

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
struct CFNotificationName
```

```c
typedef CFStringRef CFNotificationName;
```

## Topics

### Type Properties
- [static let cfLocaleCurrentLocaleDidChange: CFNotificationName!](./cfnotificationname/cflocalecurrentlocaledidchange.md)
  Identifier for the notification sent if the current locale changes.
- [static let cfTimeZoneSystemTimeZoneDidChange: CFNotificationName!](./cfnotificationname/cftimezonesystemtimezonedidchange.md)
  Name of the notification posted when the system time zone changes.
### Initializers
- [init(CFString)](./cfnotificationname/init%28_%29.md)
- [init(rawValue: CFString)](./cfnotificationname/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Types
- [typealias CFAllocatorTypeID](./cfallocatortypeid.md)
- [struct CFCalendarIdentifier](./cfcalendaridentifier.md)
- [struct CFDateFormatterKey](./cfdateformatterkey.md)
- [typealias CFErrorDomain](./cferrordomain.md)
- [struct CFLocaleIdentifier](./cflocaleidentifier.md)
- [struct CFLocaleKey](./cflocalekey.md)
- [struct CFNumberFormatterKey](./cfnumberformatterkey.md)
- [struct CFRunLoopMode](./cfrunloopmode.md)
- [struct CFStreamPropertyKey](./cfstreampropertykey.md)
- [typealias CFTypeRef](./cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationname)*