# SCDynamicStoreContext

**Framework**: System Configuration  
**Kind**: struct

Structure containing user-specified data and callbacks for a dynamic store session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct SCDynamicStoreContext
```

## Topics

### Initializers
- [init()](scdynamicstorecontext/init.md)
  Creates a dynamic store context.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](scdynamicstorecontext/init(version:info:retain:release:copydescription:).md)
  Creates a dynamic store context with the specified values.
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?](scdynamicstorecontext/copydescription.md)
  The callback used to provide a description of the `info` field.
- [var info: UnsafeMutableRawPointer?](scdynamicstorecontext/info.md)
  A C pointer to a user-specified block of data.
- [var release: ((UnsafeRawPointer) -> Void)?](scdynamicstorecontext/release.md)
  The callback used to remove a retain previously added for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value of this parameter can be `NULL`.
- [var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?](scdynamicstorecontext/retain.md)
  The callback used to add a retain for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value of this parameter can be `NULL`.
- [var version: CFIndex](scdynamicstorecontext/version.md)
  The version number of the structure type being passed in as a parameter to the `SCDynamicStore` creation function (such as [`SCDynamicStoreCreate(_:_:_:_:)`](scdynamicstorecreate(_:_:_:_:).md)). This structure is version `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias SCDynamicStoreCallBack](scdynamicstorecallback.md)
  Callback used when notification of changes made to the dynamic store is delivered.
- [class SCDynamicStore](scdynamicstore.md)
  The handle to an open dynamic store session with the system configuration daemon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext)*