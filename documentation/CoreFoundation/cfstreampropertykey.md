# CFStreamPropertyKey

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
struct CFStreamPropertyKey
```

## Topics

### Type Properties
- [static let appendToFile: CFStreamPropertyKey!](cfstreampropertykey/appendtofile.md)
  Value is a `CFBoolean` value that indicates whether to append the written data to a file, if it already exists, rather than to replace its contents.
- [static let dataWritten: CFStreamPropertyKey!](cfstreampropertykey/datawritten.md)
  Value is a `CFData` object that contains all the bytes written to a writable memory stream. You cannot modify this value.
- [static let fileCurrentOffset: CFStreamPropertyKey!](cfstreampropertykey/filecurrentoffset.md)
  Value is a `CFNumber` object containing the current file offset.
- [static let socketNativeHandle: CFStreamPropertyKey!](cfstreampropertykey/socketnativehandle.md)
  Value is a `CFData` object that contains the native handle for a socket stream—of type [`CFSocketNativeHandle`](cfsocketnativehandle.md)—to which the socket stream is connected.
- [static let socketRemoteHostName: CFStreamPropertyKey!](cfstreampropertykey/socketremotehostname.md)
  Value is a `CFString` object containing the name of the host to which the socket stream is connected or `NULL` if unknown.
- [static let socketRemotePortNumber: CFStreamPropertyKey!](cfstreampropertykey/socketremoteportnumber.md)
  Value is a `CFNumber` object containing the remote port number to which the socket stream is connected or `NULL` if unknown.
### Initializers
- [init(CFString)](cfstreampropertykey/init(_:).md)
- [init(rawValue: CFString)](cfstreampropertykey/init(rawvalue:).md)

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
- [struct CFRunLoopMode](cfrunloopmode.md)
- [typealias CFTypeRef](cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreampropertykey)*