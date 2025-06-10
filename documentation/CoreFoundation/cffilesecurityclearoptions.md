# CFFileSecurityClearOptions

**Framework**: Core Foundation  
**Kind**: struct

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CFFileSecurityClearOptions
```

## Topics

### Constants
- [static var accessControlList: CFFileSecurityClearOptions](cffilesecurityclearoptions/accesscontrollist.md)
  Clear the access control list.
- [static var group: CFFileSecurityClearOptions](cffilesecurityclearoptions/group.md)
  Clear the (POSIX) group ID.
- [static var groupUUID: CFFileSecurityClearOptions](cffilesecurityclearoptions/groupuuid.md)
  Clear the group UUID (for the access control list).
- [static var mode: CFFileSecurityClearOptions](cffilesecurityclearoptions/mode.md)
  Clear the file’s mode (POSIX permissions).
- [static var owner: CFFileSecurityClearOptions](cffilesecurityclearoptions/owner.md)
  Clear the (POSIX) owner ID.
- [static var ownerUUID: CFFileSecurityClearOptions](cffilesecurityclearoptions/owneruuid.md)
  Clear the owner UUID (for the access control list).
### Initializers
- [init(rawValue: CFOptionFlags)](cffilesecurityclearoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [enum CFRunLoopRunResult](cfrunlooprunresult.md)
- [struct CFURLEnumeratorOptions](cfurlenumeratoroptions.md)
  Options for controlling enumerator behavior.
- [enum CFURLEnumeratorResult](cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.
- [enum CGRectEdge](cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)*