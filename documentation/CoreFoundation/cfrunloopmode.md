# CFRunLoopMode

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
struct CFRunLoopMode
```

```c
typedef CFStringRef CFRunLoopMode;
```

## Topics

### Type Properties
- [static let commonModes: CFRunLoopMode!](./cfrunloopmode/commonmodes.md)
  Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [`CFRunLoopAddCommonMode(_:_:)`](./cfrunloopaddcommonmode%28_,_%29.md).
- [static let defaultMode: CFRunLoopMode!](./cfrunloopmode/defaultmode.md)
  Run loop mode that should be used when a thread is in its default, or idle, state, waiting for an event. This mode is used when the run loop is started with [`CFRunLoopRun()`](./cfrunlooprun%28%29.md).
### Initializers
- [init(CFString)](./cfrunloopmode/init%28_%29.md)
- [init(rawValue: CFString)](./cfrunloopmode/init%28rawvalue%29.md)

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
- [struct CFNotificationName](./cfnotificationname.md)
- [struct CFNumberFormatterKey](./cfnumberformatterkey.md)
- [struct CFStreamPropertyKey](./cfstreampropertykey.md)
- [typealias CFTypeRef](./cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.
- [CGFloat](./cgfloat-c.typealias.md)
  The basic type for all floating-point values.
- [HRESULT](./hresult.md)
- [LPVOID](./lpvoid.md)
- [REFIID](./refiid.md)
- [ULONG](./ulong.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopmode)*