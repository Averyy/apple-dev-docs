# SCDynamicStoreCallBack

**Framework**: System Configuration  
**Kind**: typealias

Callback used when notification of changes made to the dynamic store is delivered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias SCDynamicStoreCallBack = (SCDynamicStore, CFArray, UnsafeMutableRawPointer?) -> Void
```

## Topics

### Fields
- [store](1807875-store.md)
  The dynamic store session.
- [changedKeys](1807876-changedkeys.md)
  The list of changed keys.
- [info](1807877-info.md)
  A C pointer to a user-specified block of data.

## See Also

- [struct SCDynamicStoreContext](scdynamicstorecontext.md)
  Structure containing user-specified data and callbacks for a dynamic store session.
- [class SCDynamicStore](scdynamicstore.md)
  The handle to an open dynamic store session with the system configuration daemon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecallback)*