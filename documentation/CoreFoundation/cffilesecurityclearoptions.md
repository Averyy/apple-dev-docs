# CFFileSecurityClearOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum CFFileSecurityClearOptions : CFOptionFlags;
```

## Topics

### Constants
- [static var accessControlList: CFFileSecurityClearOptions](./cffilesecurityclearoptions/accesscontrollist.md)
  Clear the access control list.
- [static var group: CFFileSecurityClearOptions](./cffilesecurityclearoptions/group.md)
  Clear the (POSIX) group ID.
- [static var groupUUID: CFFileSecurityClearOptions](./cffilesecurityclearoptions/groupuuid.md)
  Clear the group UUID (for the access control list).
- [static var mode: CFFileSecurityClearOptions](./cffilesecurityclearoptions/mode.md)
  Clear the file’s mode (POSIX permissions).
- [static var owner: CFFileSecurityClearOptions](./cffilesecurityclearoptions/owner.md)
  Clear the (POSIX) owner ID.
- [static var ownerUUID: CFFileSecurityClearOptions](./cffilesecurityclearoptions/owneruuid.md)
  Clear the owner UUID (for the access control list).
### Initializers
- [init(rawValue: CFOptionFlags)](./cffilesecurityclearoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [struct CFISO8601DateFormatOptions](./cfiso8601dateformatoptions.md)
- [enum CFRunLoopRunResult](./cfrunlooprunresult.md)
- [struct CFURLEnumeratorOptions](./cfurlenumeratoroptions.md)
  Options for controlling enumerator behavior.
- [enum CFURLEnumeratorResult](./cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](./cfurlenumeratorgetnexturl%28_,_,_%29.md) function.
- [enum CGRectEdge](./cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)*