# SCPreferencesContext

**Framework**: System Configuration  
**Kind**: struct

A structure containing user-specified data and callbacks for accessing system configuration preferences.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct SCPreferencesContext
```

## Topics

### Initializers
- [init()](scpreferencescontext/init.md)
  Creates a preferences context.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](scpreferencescontext/init(version:info:retain:release:copydescription:).md)
  Creates a preferences context with the specified raw values.
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?](scpreferencescontext/copydescription.md)
  The callback used to provide a description of the `info` field.
- [var info: UnsafeMutableRawPointer?](scpreferencescontext/info.md)
  A C pointer to a user-specified block of data.
- [var release: ((UnsafeRawPointer) -> Void)?](scpreferencescontext/release.md)
  The calllback used to remove a retain previously added for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value may be `NULL`.
- [var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?](scpreferencescontext/retain.md)
  The callback used to add a retain for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value may be `NULL`.
- [var version: CFIndex](scpreferencescontext/version.md)
  The version number of the structure type being passed in as a parameter to [`SCPreferencesSetCallback(_:_:_:)`](scpreferencessetcallback(_:_:_:).md). This structure is version `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class SCPreferences](scpreferences.md)
  The handle to an open preferences session for accessing system configuration preferences.
- [typealias SCPreferencesCallBack](scpreferencescallback.md)
  Type of the callback function used when the preferences have been updated or applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext)*