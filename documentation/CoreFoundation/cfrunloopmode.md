# CFRunLoopMode

**Framework**: Core Foundation  
**Kind**: struct

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
struct CFRunLoopMode
```

## Topics

### Type Properties
- [static let commonModes: CFRunLoopMode!](cfrunloopmode/commonmodes.md)
  Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [`CFRunLoopAddCommonMode(_:_:)`](cfrunloopaddcommonmode(_:_:).md).
- [static let defaultMode: CFRunLoopMode!](cfrunloopmode/defaultmode.md)
  Run loop mode that should be used when a thread is in its default, or idle, state, waiting for an event. This mode is used when the run loop is started with [`CFRunLoopRun()`](cfrunlooprun().md).
### Initializers
- [init(CFString)](cfrunloopmode/init(_:).md)
- [init(rawValue: CFString)](cfrunloopmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CFAllocatorTypeID](cfallocatortypeid.md)
- [struct CFCalendarIdentifier](cfcalendaridentifier.md)
- [struct CFDateFormatterKey](cfdateformatterkey.md)
- [typealias CFErrorDomain](cferrordomain.md)
- [struct CFLocaleIdentifier](cflocaleidentifier.md)
- [struct CFLocaleKey](cflocalekey.md)
- [struct CFNotificationName](cfnotificationname.md)
- [struct CFNumberFormatterKey](cfnumberformatterkey.md)
- [struct CFStreamPropertyKey](cfstreampropertykey.md)
- [typealias CFTypeRef](cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopmode)*